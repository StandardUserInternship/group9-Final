from flask import Flask, render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.form import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from pandasql import sqldf


pysqldf = lambda q: sqldf(q, globals())
df = pd.read_csv('train.csv')
print(df)
dfs = df[0:10]
print(dfs)

avgAge = df.Age.mean()
avgFare= df.Fare.mean()
male = df['Sex'].value_counts().male
female = df['Sex'].value_counts().female
all =df.Sex.count()
maleCount=((male/all)*100).round(0)
femaleCount= 100-maleCount

print("Average age:", avgAge)
print("Average Fare:", avgFare)
print("Males in Train:", maleCount)
print("Females in Train:",femaleCount)
print(User.query.all())

data = [avgAge, avgFare, maleCount, femaleCount]
posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts, data=data)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        pw= User.query.filter_by(password=form.password.data).first()
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))

        elif user and pw:
            login_user(user, remember=form.remember.data)
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


