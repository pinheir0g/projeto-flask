from natal_delivery.ext.db import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.Unicode)
    email = db.Column("email", db.Unicode, unique=True)
    passwd = db.Column("passwd", db.Unicode)
    admin = db.Column("admin", db.Boolean, default=False)

    def __repr__(self):
        return self.email