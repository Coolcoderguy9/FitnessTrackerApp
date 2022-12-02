#user inputs info regarding gender, weight, height, desired athletic goals, etc;
#presents user with data when prompted

from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__, template_folder = 'templates')
app.static_folder = 'static'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fit.db'
app.config['SECRET_KEY'] = '7429d1b52233efdcbf08f149'
db = SQLAlchemy(app)
flask_bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
from fit import routes



