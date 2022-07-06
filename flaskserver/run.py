from flaskserver import app

# this will let the program be run on python command line without useing "flask run"
# running in debug mode so changes can be made on the fly without restarting app.
if __name__ == '__main__':
    app.run(debug=True)
