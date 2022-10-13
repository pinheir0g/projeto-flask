from flask_admin.contrib.sqla import ModelView
from flask_admin.actions import action
from flask_admin.contrib.sqla import filters
from natal_delivery.ext.auth.models import User
from natal_delivery.ext.db import db
from flask import flash

#def format_user(self, request, user, *args):
#   return user.email.split("@")[0]

class UserAdmin(ModelView):
    """Users admin interface"""

     # column_formatters = {"email": lambda s, r, u, *a: u.email.split("@")[0]}

    column_list = ["email", "admin"]

    column_searchable_list = ["email"]

    column_filters = [
        "email",
        "admin",
        filters.FilterLike(
            User.email,
            "dominio",
            options=(("gmail", "Gmail"), ("outlook", "Outlook"))
        )
     ]
 
    can_edit = False
    can_create = True
    can_delete = True

    @action(
        'toggle_admin',
        'Toggle admin status',
        'Are you sure?'
    )

    def toggle_admin_status(self, ids):
        users = User.query.filter(User.id.in_(ids)).all()
        for user in users:
            user.admin = not user.admin
        db.session.commit()
        flash(f" {len(users)} Usuários alterados com sucesso", "success")

    

    @action(
        'send_email',
        'Send email to all users',
        'Are you sure?'
    )

    def send_email(self, ids):
        users = User.query.filter(User.id.in_(ids)).all()
        # 1) redirect para um form para escrever a mensagem do email
        # 2) enviar o email
        flash(f" {len(users)} Emails enviados", "success")