# static folder will contain the css and images and other decorative elements
# templates folder will contain the html codes
# / -home page, /userform -user books service here
# /admin -admin can view service list here

from churchRegistration import app, login_manager,db, mail
from churchRegistration.models import *
from flask import Flask, render_template, redirect, url_for, flash, request
from churchRegistration.forms import *
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Message


@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html', page_title='Home')


@app.route('/userform')
def userform():
    form = JoinServiceForm()
    return render_template('userform.html', page_title = "Register for a service", form = form)


@app.route('/admin/createaccount', methods=['GET', 'POST'])
def admin_account():
    form = AdminRegister()
    if form.validate_on_submit():
        user = User(form.church_name.data, form.email.data, form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('admin_register.html', page_title='Register Church', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = AdminLogin()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user.check_password(form.password.data) and user is not None:
            login_user(user, remember=form.remember.data)
            next = request.args.get('next')
            if next == None or not next[0] == '/':
                next = url_for('admin')
            return redirect(next)
    return render_template('admin.html', page_title='Admin Login', form=form)


@app.route('/admin/AdminAddService', methods = ['GET','POST'])
@login_required
def add_service():
    form = CreateChurchServiceForm()
    if form.validate_on_submit():
        # service = ChurchService(form.name.data, form.date.data, )
        flash("Service Successfully Added")
        return redirect(url_for("admin"))
    return render_template("add_service.html", page_title = "Add a Service", form = form)

@app.route('/admin')
@login_required
def admin():
    services = ChurchService.query.filter_by(church_id = current_user.id).all()
    if len(services) == 0:
        services = 0
    return render_template('dashboard.html', page_title = {current_user.name}, services = services)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


def send_reset_email(user):
    token = user.get_token()
    msg = Message('Password Reset Request', sender='noreply@demo.com', recipients=[user.email])
    msg.body = f'''Click the following link to reset your password
    {url_for('reset_token', token=token, _external=True)} 
    If you did not make this request please ignore
    '''
    mail.send(msg)


@app.route('/reset_password', methods=['GET','POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('admin'))
    form = RequestReset()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password', 'info')
        return redirect(url_for('login'))
    return render_template('reset_request.html', page_title='Reset Password',form=form)


@app.route('/reset_password/<token>', methods=['GET','POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('admin'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('This is an invalid or expired token', 'warning')
        return redirect(url_for('reset_request'))
    form = ResetPassword()
    if form.validate_on_submit():
        #possible error password doesn't change/flash messages do not appear
        user = User(password=form.password.data)
        db.session.commit()
        flash('Your password has been successfully reset', 'success')
        return redirect(url_for('login'))
    return render_template('reset_token.html', page_title='Reset Password', form=form)



if __name__ == '__main__':
    app.run(debug = True)