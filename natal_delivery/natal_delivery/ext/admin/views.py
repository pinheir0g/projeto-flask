from flask_admin.contrib.sqla import ModelView
from flask_admin.actions import action
from natal_delivery.ext.db import db
from natal_delivery.ext.db import models  # noqa
from flask import flash


class Category(ModelView):
    """Category interface"""

    column_list = ["name", "on_menu"]


class Store(ModelView):
    """Store interface"""


class Items(ModelView):
    """Store interface"""


class Store(ModelView):
    """Store interface"""