from flask import Flask
from flask_login import login_required
from backend.config import LocalDevelopmentConfig
from backend.models import db, User, Role
from flask_security import Security, SQLAlchemyUserDatastore, auth_required
from flask_caching import Cache
from backend.celery.celery_factory import celery_init_app
import flask_excel as excel


def createApp():
    app = Flask(__name__, template_folder='frontend', static_folder='frontend', static_url_path='/static')

    app.config.from_object(LocalDevelopmentConfig)


    # model init
    db.init_app(app)
    
    # cache init
    cache = Cache(app)


    #flask security
    datastore = SQLAlchemyUserDatastore(db, User, Role)
    app.cache = cache

    app.security = Security(app, datastore=datastore, register_blueprint=False)
    app.app_context().push()

    from backend.resources import api
    # flask-restful init
    api.init_app(app)

    return app

app = createApp()

celery_app = celery_init_app(app)

import backend.create_initial_data

import backend.routes

import backend.celery.celery_schedule

excel.init_excel(app)

if (__name__ == '__main__'):
    # flask-excel
    app.run()

