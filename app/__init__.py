import os

from flask import Flask


def create_app():
    # create and configure the app
    app = Flask(__name__, static_folder="") 
    
    # Register blueprints
    from app.routes import home
    app.register_blueprint(home)

    return app
