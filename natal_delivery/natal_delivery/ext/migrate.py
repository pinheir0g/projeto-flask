from flask_migrate import Migrate
from natal_delivery.ext.db import db #noqa
from natal_delivery.ext.db import models

migrate = Migrate()


def init_app(app):
    migrate.init_app(app, db)
