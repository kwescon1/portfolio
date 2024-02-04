# This '__init__.py' file is where you'll define a Flask factory function.
# The factory function is used to create and configure the Flask application instance.
# Within this function, you'll link all your Flask blueprints and set up the app.

from flask import Flask
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    
    # Initialize Flask extensions here
    
    #Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app
    