# app > __init__.py

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
lm = LoginManager()

# initialize SQLalchemy models
from . import models


def create_app():

    app = Flask(__name__)
    app.config.from_object('config.Config')

    toolbar = DebugToolbarExtension(app)

    db.init_app(app)

    lm.login_view = 'login'
    lm.init_app(app)

    with app.app_context():

        from . import routes
        from .project import bp as project_bp
        from .profile import bp as profile_bp

        app.register_blueprint(profile_bp, url_prefix='/u')
        app.register_blueprint(project_bp, url_prefix='/p')

        # db.drop_all()
        db.create_all()

        return app
