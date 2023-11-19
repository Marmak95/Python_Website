from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

"""
This is the back-end that initializes the application with the database.
"""

db = SQLAlchemy()
DB_NAME = "database.db"

def readSecretPassword():
    with open("website/secretAppKey.cfg", "r") as file:
        password = file.read().strip()
        file.close()
        return password

def createApp():
    app = Flask(__name__)

    # Read the secret password from the configuration file (secretAppKey.cfg)
    secretPassword = readSecretPassword()

    app.config["SECRET_KEY"] = secretPassword
    # Store the database in the website folder
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User, Note

    createDatabase(app)

    loginManager = LoginManager()
    # Where to go when the user is not logged in.
    loginManager.login_view = "auth.login"
    loginManager.init_app(app)

    # Use this function to load the user, looks for the primary key.
    @loginManager.user_loader
    def loadUser(id):
        return User.query.get(int(id))

    return app

def createDatabase(app):
    if(not path.exists("website/" + DB_NAME)):
        with app.app_context():
            db.create_all()
        print("Database was created.")
