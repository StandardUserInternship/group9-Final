from flask import Flask, render_template, url_for

from Forms import LoginForm, RegistrationForm

app = Flask(__name__)


app.config['SECRET KEY'] = 'dd74d77daecfe64f22d4a5c7a1b8ffa4'

# this is the main home page
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


# Content Page 
@app.route("/content")
def content():
    return render_template('content.html', title ='content')


# Login Page
@app.route("/login")
def login():
    form = LoginForm
    return render_template('login.html', title='login', form = form)


# register Page
@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='register', form = form)


# Admin page
@app.route("/admin")
def admin():
    return render_template('', title='Admin')





# this will let the program be run on python command line without useing "flask run"
# running in debug mode so changes can be made on the fly without restarting app.
if __name__ == '__main__':
    app.run(debug=True)
