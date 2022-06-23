from flask import Flask, render_template, url_for
app = Flask(__name__)

# this is the main home page
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


# Content Page 
@app.route("/content")
def content():
    return render_template('content.html', title='content')


# Login Page
@app.route("/login")
def login():
    return render_template('', title='login')


# Login Page
@app.route("/register")
def register():
    return render_template('', title='register')


# Admin page
@app.route("/admin")
def admin():
    return render_template('', title='Admin')





# this will let the program be run on python command line without useing "flask run"
# running in debug mode so changes can be made on the fly without restarting app.
if __name__ == '__main__':
    app.run(debug=True)
