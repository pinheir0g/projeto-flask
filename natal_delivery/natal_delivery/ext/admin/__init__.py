from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from natal_delivery.ext.db import db
from natal_delivery.ext.db import models
from natal_delivery.ext.admin import views


admin = Admin() 


def init_app(app):
    admin.name = app.config.get("ADMIN_NAME", "Natal Refeições")
    admin.template_mode = "bootstrap2"
    admin.init_app(app)

    admin.add_view(ModelView(models.Category, db.session))
    admin.add_view(ModelView(models.Store, db.session))
    admin.add_view(ModelView(models.Items, db.session))
    admin.add_view(ModelView(models.Order, db.session))
    admin.add_view(ModelView(models.OrderItems, db.session))
    admin.add_view(ModelView(models.Checkout, db.session))
    admin.add_view(ModelView(models.Address, db.session))