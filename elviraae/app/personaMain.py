'''
Created on 18/2/2015

@author: PC06
'''
from app import  app
from ec.edu.itsae.dao import PersonaDAO
from flask import render_template, request, redirect, url_for


@app.route("/mainpersona")
def mainPersona():
    objr=PersonaDAO.PersonaDao().reportarPersona()    
    return render_template("prueba.html", data=objr)


@app.route("/addPersona", methods=['POST'])
def addPersona():
    nombre=request.form.get('nombre', type=str)
    apaterno=request.form.get('apaterno', type=str)
    amaterno=request.form.get('amaterno', type=str)
    cedula=request.form.get('cedula', type=str)
    fnacimiento=request.form.get('fnacimiento', type=str)
    sexo=request.form.get('sexo', type=str)
    direccion=request.form.get('direccion', type=str)
    celular=request.form.get('celular', type=str)
    estado=request.form.get('estado', type=int)


    PersonaDAO.PersonaDao().insertarPersona(nombre, apaterno, amaterno, cedula, fnacimiento, sexo, direccion, celular, estado)
    return redirect(url_for('mainPersona'))



@app.route("/deletePersona", methods=['POST'])
def deletePersona():
    nombre=request.form.get('nombre', type=str)
    apaterno=request.form.get('apaterno', type=str)
    amaterno=request.form.get('amaterno', type=str)
    cedula=request.form.get('cedula', type=str)
    fnacimiento=request.form.get('fnacimiento', type=str)
    sexo=request.form.get('sexo', type=str)
    direccion=request.form.get('direccion', type=str)
    celular=request.form.get('celular', type=str)
    estado=request.form.get('estado', type=int)


    PersonaDAO.PersonaDao().eliminarPersona(nombre, apaterno, amaterno, cedula, fnacimiento, sexo, direccion, celular, estado)
    return redirect(url_for('mainPersona'))



@app.route("/updatePersona", methods=['POST'])
def updatePersona():
    nombre=request.form.get('nombre', type=str)
    apaterno=request.form.get('apaterno', type=str)
    amaterno=request.form.get('amaterno', type=str)
    cedula=request.form.get('cedula', type=str)
    fnacimiento=request.form.get('fnacimiento', type=str)
    sexo=request.form.get('sexo', type=str)
    direccion=request.form.get('direccion', type=str)
    celular=request.form.get('celular', type=str)
    estado=request.form.get('estado', type=int)


    PersonaDAO.PersonaDao().editarPersona(nombre, apaterno, amaterno, cedula, fnacimiento, sexo, direccion, celular, estado)
    return redirect(url_for('mainPersona'))


@app.route("/buscarauto")
def buscarPersonaAuto():
    nombre=str(request.args.get('term'))
    objr=PersonaDAO.PersonaDao().buscarPersonaNombre(nombre) 
    print objr
    return objr   
   

@app.route("/mostrarauto")
def buscarPersonaDato():
    nombre=str(request.args.get('bnombre'))
    objr=PersonaDAO.PersonaDao().buscarPersonaDato(nombre) 
    return render_template("prueba.html", data=objr)

#def buscarPersonaDato():
#    nombre=str(request.args.get('bnombre'))
#    objR=PersonaDao.PersonaDao().buscarPersonaDato(nombre)
#    return render_template("prueba.html", data=objR)