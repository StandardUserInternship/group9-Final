from flask import Flask

app = Flask(__name__)

# this is the main home page
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# this will let the program be run on python command line without useing "flask run"
# running in debug mode so changes can be made on the fly without restarting app.
if __name__ == '__main__':
    app.run(debug=True)
