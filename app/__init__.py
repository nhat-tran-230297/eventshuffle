from importlib import import_module

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

MODULES_BLUEPRINTS = ['base']

db = SQLAlchemy()
migrate = Migrate()

def register(app): 
    """ register for apps """

    for module_name in MODULES_BLUEPRINTS:
        module = import_module(f'app.{module_name}.views')
        app.register_blueprint(module.blueprint)


def configure_database(app):
    """ create database only once before the app runs"""

    @app.before_first_request
    def initialize_database():    
        db.create_all()


    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()


def create_app(config):
    app = Flask(__name__)

    # set up configuration
    app.config.from_object(config)

    # initialize db
    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)

    register(app)
    configure_database(app)
    

    return app