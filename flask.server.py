from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy 
from Forms import LoginForm, RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dd74d77daecfe64f22d4a5c7a1b8ffa4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)






# this will let the program be run on python command line without useing "flask run"
# running in debug mode so changes can be made on the fly without restarting app.
if __name__ == '__main__':
    app.run(debug=True)
