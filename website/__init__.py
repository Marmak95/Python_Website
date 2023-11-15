from flask import Flask

def createApp():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "secretkey123"
    
    return app