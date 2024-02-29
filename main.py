from flask import Flask, render_template, request #importe de las librerias
from flask import flash
from flask_wtf.csrf import CSRFProtect
from flask import g
from config import DevelopmentConfig
from models import db, Alumnos
import forms

app=Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

@app.route("/")
def load():
    return render_template("index.html")

@app.route("/ABC_Completo", methods=["GET", "POST"])
def abc():
    alumForm = forms.UserForm2(request.form)
    alumno = Alumnos.query.all()

    return render_template("ABC_Completo.html", alumnos = alumno)

@app.route("/index", methods=["GET", "POST"])
def index():
    create_form = forms.UserForm2(request.form)
    if request.method == "POST":
        alum = Alumnos(
            nombre=create_form.nombre.data,
            apaterno = create_form.apaterno.data,
            amaterno = create_form.amaterno.data,
            email=create_form.email.data
            )
        db.session.add(alum)
        db.session.commit()
    return render_template("index.html", form=create_form)

@app.route("/alumnos", methods=["GET", "POST"])
def alumnos():
    alumno_clase = forms.UserForm(request.form)
    nom=""    
    apeP=""
    apeM="" 
    email=""
    edad=0
    if request.method == "POST" and alumno_clase.validate():
        nom=alumno_clase.nombre.data
        apeP=alumno_clase.apaterno.data
        apeM=alumno_clase.amaterno.data
        email=alumno_clase.email.data
        edad=alumno_clase.edad.data
        
        mensaje = "Bienvenido {}".format(nom)
        flash(mensaje)

    return render_template("alumnos.html", form=alumno_clase, nom=nom, apep=apeP, apem=apeM, email=email, edad=edad)

@app.errorhandler(404)
def errorHandler(ex):
    return render_template("404.html"),404

if __name__=="__main__":
    csrf.init_app(app)
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
    app.run()