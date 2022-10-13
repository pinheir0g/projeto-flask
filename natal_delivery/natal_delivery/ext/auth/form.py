import wtforms as wtf
from flask_wtf import FlaskForm


class UserForm(FlaskForm):
    email = wtf.StringField('Email', [wtf.validators.DataRequired(), wtf.validators.Email()])
    password = wtf.PasswordField('Senha', [wtf.validators.DataRequired()])