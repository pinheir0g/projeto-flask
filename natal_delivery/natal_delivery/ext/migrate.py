from flask_migrate import Migrate
from natal_delivery.ext.db import db #noqa

migrate = Migrate()


def init_app(app):
    migrate.init_app(app, db)
