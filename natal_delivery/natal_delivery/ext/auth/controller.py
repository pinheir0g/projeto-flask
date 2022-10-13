from werkzeug.security import generate_password_hash

from natal_delivery.ext.auth.models import User
from natal_delivery.ext.db import db

ALG = "pbkdf2:sha256"

def create_user(email: str, passwd: str, admin: bool = False) -> User:
    user = User(
        email=email,
        passwd = generate_password_hash(passwd, ALG),
        admin=admin

    )
    db.session.add(user)
    # TODO: Tratar exception caso user ja exista
    db.session.commit()
    return user
