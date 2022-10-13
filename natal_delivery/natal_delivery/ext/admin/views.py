from flask_admin.contrib.sqla import ModelView, filters
from flask_admin.actions import action
from natal_delivery.ext.db import db
from natal_delivery.ext.db import models  # noqa
from flask import flash


class Category(ModelView):
    """Category interface"""

    column_list = ["name", "on_menu"]


class Items(ModelView):
    """Store interface"""
    column_formatters = {"price": lambda s, r, u, *a: i.price}

class Order(ModelView):
    """Store interface"""


class OrderItems(ModelView):
    """Store interface"""


class Checkout(ModelView):
    """Store interface"""


class Address(ModelView):
    """Store interface"""
