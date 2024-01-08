from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = '1af6217ac4e6afb3dd2006c6a9a5596d'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///siteitems.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
Login_manager = LoginManager(app)

from flaskblog import routes 