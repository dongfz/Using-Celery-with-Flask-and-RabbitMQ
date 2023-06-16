import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app() -> Flask:
    _env = os.getenv('FLASK_ENV')
    flask_app = Flask(__name__, instance_relative_config=True)
    flask_app.config.from_pyfile('config.%s.py' % _env, silent=True)
    db.init_app(flask_app)
    return flask_app
