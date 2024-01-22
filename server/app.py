from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


# App Initialization
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mellon'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///atlas.db?timeout=10'

# Database Initialization
db = SQLAlchemy(app)

# Login Initialization
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'