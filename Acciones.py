from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from database import Database
from database import engine
from database import db_session
from flask import url_for
import models

app = Flask(__name__)
    
Database.metadata.create_all(engine)

@app.get('/') 
def home():   
    alumno = db_session.query(models.alumnos).all()
    return render_template("home.html", lista_alumno=alumno)


@app.post('/insertar')
def insertar():
    name = request.form['nombre']
    app = request.form['apellido']
    materia = request.form['materia']
    presente = request.form['presente']
    
    nuevo_alumno = models.alumnos(
        nombre = name,
        apellidos = app,
        materia = materia,
        presente = presente,
    )
    db_session.add(nuevo_alumno)
    db_session.commit()
    return redirect("/")

@app.get('/eliminar/<id>')
def eliminar(id):
   alumno = db_session.query(models.alumnos).get(id)
   
   if alumno == None:
       flash('ID no encontrado')
       return render_template('home.html')
   
   db_session.delete(alumno)
   db_session.commit()
   
   return redirect(url_for('home'))  
   
@app.post('/actualizar/<id>')
def actualizar(id):
    alumno = db_session.query(models.alumnos).get(id)
       
    if alumno == None:
        flash('ID no encontrado')
        return redirect (url_for('home'))
       
    nomb = request.form['name']
    apps = request.form['apps']
    materia = request.form['materia']
    presente = request.form['presente']
       
    if alumno == None:
        flash('No hay nada')
        return redirect (url_for('home'))
       
    alumno.nombre = nomb
    alumno.apellidos = apps
    alumno.materia = materia
    alumno.presente = presente
       
    db_session.add(alumno)
    db_session.commit()
       
    return redirect(url_for('home'))
   
   
   
if __name__ == '__main__':
    app.run('0.0.0.0', 8585, debug=True)
    
    