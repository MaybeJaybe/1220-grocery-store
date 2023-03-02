from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from grocery_app.config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

# is extensions.py supposed to be __init__.py? tutorial says __init__.py but it doesnt exist...
# also the auth lab has it in extensions.py so i just put it here. hope it works

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from .models import User

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(user_id)

bcrypt = Bcrypt(app)