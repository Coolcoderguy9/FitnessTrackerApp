from fit import db, login_manager
from fit import flask_bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String(), nullable = False, unique = True)
    email_address = db.Column(db.String(), nullable = False, unique = True)
    password = db.Column(db.String(), nullable = False)

    @property
    def password_hsh(self):
        return self.password_hsh

    @password_hsh.setter
    def password_hsh(self, plain_text_password):
        self.password = flask_bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return flask_bcrypt.check_password_hash(self.password, attempted_password)

class Program(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(), nullable = False, unique = True)
    description = db.Column(db.String(), nullable = False, unique = True)
