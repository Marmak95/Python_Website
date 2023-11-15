from flask import Flask

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

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app
