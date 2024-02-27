from wtforms import Form
from flask_wtf import FlaskForm

from wtforms import StringField, IntegerField, EmailField

from wtforms import validators 

class UserForm(Form):
    id = IntegerField('id', [validators.number_range(min=1, max=20, message="Valor no valido")])
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

class UserForm2(Form):
    id = IntegerField('id', [validators.number_range(min=1, max=20, message="Valor no valido")])
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