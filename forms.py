from wtforms import Form
from flask_wtf import FlaskForm

from wtforms import StringField, IntegerField, EmailField

from wtforms import validators 

class UserForm(Form):
    nombre=StringField("nombre", validators=[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4, max=15, message="Ingresa un nombre válido")
    ])
    apaterno=StringField("apaterno", validators=[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4, max=15, message="Ingresa un nombre válido")
    ])
    amaterno=StringField("amaterno", validators=[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4, max=15, message="Ingresa un nombre válido")
    ])
    
    email=EmailField("email", validators=[
        validators.Email(message="Ingrese un correo válido")
    ])
    edad=IntegerField("edad", validators=[
        validators.DataRequired(message='El campo es requerido')
    ])