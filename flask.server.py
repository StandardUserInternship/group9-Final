from flask import Flask, render_template, url_for, flash, redirect

from Forms import LoginForm, RegistrationForm

app = Flask(__name__)


app.config['SECRET_KEY'] = 'dd74d77daecfe64f22d4a5c7a1b8ffa4'

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
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@Final.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='login', form = form)


# register Page
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='register', form = form)


# Admin page
@app.route("/admin")
def admin():
    return render_template('', title='Admin')





# this will let the program be run on python command line without useing "flask run"
# running in debug mode so changes can be made on the fly without restarting app.
if __name__ == '__main__':
    app.run(debug=True)
