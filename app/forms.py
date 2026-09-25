from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
from app import db
from app.models import Teste
class TesteForms(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Logar')

    def save(self):
        teste = Teste(
            email = self.email.data,
            senha = self.senha.data
        )

        db.session.add(teste)
        db.session.commit()