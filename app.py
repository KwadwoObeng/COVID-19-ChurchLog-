# static folder will contain the css and images and other decorative elements
# templates folder will contain the html codes
# / -home page, /userform -user books service here
# /admin -admin can view service list here


from churchRegistration import app
from flask import Flask, render_template
from churchRegistration.forms import *

@app.route('/')
def index():
    return "Hello World"


@app.route('/userform')
def userform():
    return


@app.route('/admin')
def admin():
    return


@app.route('/admin/AdminAddService')
def add_service():
    form = CreateChurchServiceForm()
    return render_template("add_service.html", page_title = "Add a Service", form = form)


if __name__ == '__main__':
    app.run(debug = True)
