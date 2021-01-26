from importlib import import_module

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

MODULES_BLUEPRINTS = ['base', 'api']

db = SQLAlchemy()
migrate = Migrate()

def register(app): 
    for module_name in MODULES_BLUEPRINTS:
        module = import_module(f'app.{module_name}.views')
        app.register_blueprint(module.blueprint)


def configure_database(app):
    """ create database only once before the app runs"""

    @app.before_first_request
    def initialize_database():    
        db.create_all()

        # from app.models import Events, People, Dates

        # for i in range(100000):
        #     event = Events(name="Jack's party")

        #     if (i % 3) == 0:
        #         person = People()

        #     db.session.add(event)

        # db.session.commit()

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