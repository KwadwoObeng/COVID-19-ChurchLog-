# static folder will contain the css and images and other decorative elements
# templates folder will contain the html codes
# / -home page, /userform -user books service here
# /admin -admin can view service list here

from churchRegistration import app, login_manager,db
from churchRegistration.models import *
from flask import Flask, render_template, redirect, url_for
from churchRegistration.forms import *
from flask_login import login_user, login_required, logout_user
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
        return redirect(url_for('admin'))
    return render_template('admin_register.html', page_title='Register Church', form=form)


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    form = AdminLogin()
    if form.validate_on_submit():
        return redirect(url_for('add_service'))
    return render_template('admin.html', page_title='Admin Login', form=form)


@app.route('/admin/AdminAddService', methods = ['GET','POST'])
def add_service():
    form = CreateChurchServiceForm()
    if form.validate_on_submit():
        return "Service Successfully Added"
        return redirect(url_for("index"))
    return render_template("add_service.html", page_title = "Add a Service", form = form)

@app.route('/login')
def login():
    pass

if __name__ == '__main__':
    app.run(debug = True)