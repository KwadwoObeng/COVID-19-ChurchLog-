from churchRegistration import db, login_manager
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    __tablename__ = 'church'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True)
    email = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(128))
    churchservices = db.relationship('ChurchService', backref='church', lazy=True)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class ChurchService(db.Model):
    __tablename__ = 'churchService'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    date = db.Column(db.DateTime())
    number_of_attendees = db.Column(db.Integer(), default=0)
    capacity = db.Column(db.Integer(), default = 100)
    church_id = db.Column(db.Integer, db.ForeignKey('church.id'))
    attendees = db.relationship('ServiceAttendees', backref = 'service', lazy = True)

    def __init__(self, name, date, capacity, church):
        self.name = name
        self.date = date
        self.capacity = capacity
        self.church = church

    def __repr__(self):
        return f"{self.name} at {self.date}"

class ServiceAttendees(db.Model):
    __tablename__ = 'attendees'

    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(64), nullable = False)
    number = db.Column(db.String(20), nullable = False)
    area = db.Column(db.String(30), nullable = False)
    service_id = db.Column(db.Integer, db.ForeignKey('churchService.id'))

    def __init__(self, name, number, area, service):
        self.name = name
        self.number = number
        self.area = area
        self.service = service