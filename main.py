from flask import Flask, render_template, request #importe de las librerias
from flask import flash
from flask_wtf.csrf import CSRFProtect
from flask import g
from config import DevelopmentConfig
import forms

app=Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

@app.route("/") #Pagina principal 
def index():
    return render_template("index.html") #importe de archivos html

@app.route("/alumnos", methods=["GET", "POST"]) #Pantalla de alumnos
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
    
    app.run()