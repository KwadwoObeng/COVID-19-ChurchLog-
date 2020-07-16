from churchRegistration import db, login_manager
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    __tablename__ = 'church'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(), unique = True)
    email = db.Column(db.String(64), unique = True)
    password_hash = db.Column(db.String(128))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)