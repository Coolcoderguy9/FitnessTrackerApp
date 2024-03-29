from fit import app
from flask import render_template, url_for, redirect, flash, get_flashed_messages
from fit.forms import RegisterForm, LoginForm
from fit.models import User
from fit import db
from flask_login import login_user, logout_user

# routes give direction to where the user is directed when links are clicked on
# website intended to update dynamically when user inputs valid data through forms


@app.route('/')
def main():
    return render_template('home.html')

@app.route('/stats')
def user_stats():
    return render_template('stats.html')

@app.route('/goals')
def user_goals():
    return render_template('goals.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username = form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.pswd.data
        ):
            login_user(attempted_user)
            flash('Successfully logged in!', category = 'success')
            return redirect(url_for('main'))
        else:
            flash('Username and password not matching, please retry.', category = 'danger')
    return render_template('login.html', form = form)

@app.route('/logout')
def logout():
    logout_user()
    flash('Successfuly logged out!')
    return redirect(url_for('login'))

@app.route('/register', methods = ['GET', 'POST'])
def register():
    regform = RegisterForm()
    if regform.validate_on_submit():
        new_user = User(username = regform.username.data,
                        email_address = regform.email_address.data,
                        password_hsh = regform.pswd.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    if regform.errors != {}:
        for err_msg in regform.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category = 'danger')
    return render_template('register.html', regform = regform)
