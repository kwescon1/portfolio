# This '__init__.py' file is where you'll define a Flask factory function.
# The factory function is used to create and configure the Flask application instance.
# Within this function, you'll link all your Flask blueprints and set up the app.

from flask import Flask
from config import Config
from app.extensions import db,bcrypt,login_manager

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    
    # Initialize Flask extensions here
    db.init_app(app)
    bcrypt.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'
    login_manager.init_app(app)

    
    #Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.projects import bp as projects_bp
    app.register_blueprint(projects_bp,url_prefix='/projects')

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from app.admin import bp as admin_bp
    app.register_blueprint(admin_bp,url_prefix='/admin')

    return app
    