# static folder will contain the css and images and other decorative elements
# templates folder will contain the html codes
# / -home page, /userform -user books service here
# /admin -admin can view service list here

from churchRegistration import app, login_manager,db
from churchRegistration.models import *
from flask import Flask, render_template, redirect, url_for, flash, request
from churchRegistration.forms import *
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash


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
            login_user(user)
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
        flash("Service Successfully Added")
        return redirect(url_for("index"))
    return render_template("add_service.html", page_title = "Add a Service", form = form)

@app.route('/admin')
@login_required
def admin():
    return f"This is the admin page for {current_user.name}"

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug = True)