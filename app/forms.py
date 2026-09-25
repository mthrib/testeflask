from flask_wtf import Flaskform
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidarionError
from app import db
from app.models import Teste
class TesteForms(Flaskform):
    email = StringField('Email', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Logar')

    def save(self):
        teste = Teste(
            email = self.email.data,
            senha = self.senha.data
        )

        db.session.add(teste)
        db.session.comit()