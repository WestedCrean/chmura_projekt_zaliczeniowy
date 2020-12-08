from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask import request

from config import app_config

db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def hello_world():
        return 'Running, connected to database'
    
    @app.route('/users/<user_id>', methods = ['GET','DELETE'])
    def single_user(user_id):

    @app.route('/users', methods = ['GET', 'POST'])
    def users():
        if request.method == 'GET':

        if request.method == 'POST':
        
   


    login_manager.init_app(app)
    login_manager.login_message = 'You must be logged in to access this page'
    login_manager.login_view = 'auth.login'

    migrate = Migrate(app,db)
    from app import models
    return app
