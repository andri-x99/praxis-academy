from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import app_config
#BARIS SISIPAN 2
from flask_login import LoginManager
#BARIS SISIPAN 3
from flask_migrate import Migrate
#BARIS SISIPAN 5
from config import app_config
#BARIS SISIPAN 6
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
#BARIS SISIPAN 2
login_manager = LoginManager()

# Bootstrap(app)
def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    
    #BARIS SISIPAN 6
    Bootstrap(app)
    db.init_app(app)
    #BARIS SISIPAN
    # @app.route('/')
    # def hello_world():
    #     return 'Hello, World!'
    #BARIS SISIPAN 2
    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"
  
    #BARIS SISIPAN 3
    migrate = Migrate(app, db)

    from app import models

    #BARIS SISIPAN 4
    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)
    
    return app






