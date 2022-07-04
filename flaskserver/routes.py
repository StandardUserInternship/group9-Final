from flask import Flask, render_template, url_for, flash, redirect
from flaskserver import app
from flaskserver.Forms import RegistrationForm, LoginForm
from flaskserver.models import User, Post

# this is the main home/content page
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


# Login Page
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@Final.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='login', form=form)


# register Page
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='register', form=form)


# Admin page
@app.route("/admin")
def admin():
    return render_template('', title='Admin')
