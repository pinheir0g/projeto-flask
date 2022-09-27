from natal_delivery.ext.auth import models  # noqa

from natal_delivery.ext.db import db
from natal_delivery.ext.auth.admin import UserAdmin 
from natal_delivery.ext.admin import admin
from natal_delivery.ext.auth.models import User 


def init_app(app):
    """TODO: Inicializar Flask Simple Login + JWT"""
    admin.add_view(UserAdmin(User, db.session))