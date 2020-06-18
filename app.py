# static folder will contain the css and images and other decorative elements
# templates folder will contain the html codes
from churchRegistration import app
from flask import Flask

@app.route('/')
def index():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug = True)