from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model): # User class
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(90), unique=True)
    username = db.Column(db.String(30), unique=False)
    password = db.Column(db.String)
    is_admin = db.Column(db.Boolean, default=False)

    def get_id(self): # Return ID
        return self.id
    
    def set_password(self, password): # Sets password
        self.password = generate_password_hash(password)

    def check_password(self, password): # Checks password
        return check_password_hash(self.password, password)