from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from natal_delivery.ext.db import db
from natal_delivery.ext.db import models
from natal_delivery.ext.admin.views import *


admin = Admin() 


def init_app(app):
    admin.name = app.config.get("ADMIN_NAME", "Natal Refeições")
    admin.template_mode = "bootstrap2"
    admin.init_app(app)

    admin.add_view(Category(models.Category, db.session))
    admin.add_view(Items(models.Items, db.session))
    admin.add_view(Order(models.Order, db.session))
    admin.add_view(OrderItems(models.OrderItems, db.session))
    admin.add_view(Checkout(models.Checkout, db.session))
    admin.add_view(Address(models.Address, db.session))