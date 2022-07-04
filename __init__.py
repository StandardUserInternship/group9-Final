from flask import Flask
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__)
app.config['SECRET_KEY'] = 'dd74d77daecfe64f22d4a5c7a1b8ffa4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


from flaskserver import routes