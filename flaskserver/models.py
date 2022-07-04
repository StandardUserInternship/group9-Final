from datetime import datetime
from flaskserver import db

# Users Table - User ID, Account Type, User Name, Password Hash, email, Date Created, & Last Login
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    #image_file = db.Column(db.String(20), nullable=False, default= 'default.jpg')
    password = db.Column(db.String(60), nullable=False)
    post = db.relationship('Post', backref='author', lazy=True)
    date_created = db.Column(db.DateTime, nullable=False, default= datetime.utcnow)
    #last_login = 

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


# DataSets - Data Set Name, Data Set File
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')" 
