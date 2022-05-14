from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired,Email,Length

class SignupForm(FlaskForm):
    name = StringField('nombre', validators=[DataRequired(), Length(max=25)])
    #nombre viene de la vista app.py y de contacto html 
    password = PasswordField('contra', validators=[DataRequired() ])
    email =StringField('email', validators=[DataRequired(), Email()])

    #Por último especificar que este formulario de va a enviar con un submit de

    submit = SubmitField('envio_formulario')