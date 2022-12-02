from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import EqualTo, Email, DataRequired, ValidationError
from fit.models import User

#forms for various user actions on website, provide fields for user to input
#data
#have validation function to verify correct info has been submitted

class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username = username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists.')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address = email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email already taken, please provide another.')
    username = StringField(label = 'Username', validators=[DataRequired()])
    email_address = StringField(label = 'Email Address', validators=[Email(), DataRequired()])
    pswd = PasswordField(label = 'Password', validators=[DataRequired()])
    pswdcnfrm = PasswordField(label = 'Confirm password: ', validators=[EqualTo('pswd'), DataRequired()])
    submit = SubmitField(label = 'Create Account')

class LoginForm(FlaskForm):
    username = StringField(label = 'Username', validators = [DataRequired()])
    pswd = PasswordField(label = 'Password', validators = [DataRequired()])
    submit = SubmitField(label = 'Login')

class StatForm(FlaskForm):
    bench = StringField(label = 'Bench Press')
    squat = StringField(label = 'Squat')
    deadlift = StringField(label = 'Deadlift')
    mile_time = StringField(label = 'Mile Time')
    bodyfat_prcnt = StringField(label = 'Bodyfat Percentage')
    weight = StringField(label = 'Weight')
    submit = SubmitField(label = 'Update')

class GoalForm(FlaskForm):
    bench = StringField(label='Bench Press')
    squat = StringField(label='Squat')
    deadlift = StringField(label='Deadlift')
    mile_time = StringField(label='Mile Time')
    bodyfat_prcnt = StringField(label = 'Bodyfat Percentage')
    weight = StringField(label = 'Weight')
    submit = SubmitField(label = 'Update')
