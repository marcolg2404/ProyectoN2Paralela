from flask import Flask, url_for, render_template, request, flash, redirect
from flask import jsonify
from werkzeug.utils import secure_filename
from datetime import datetime
from funciones_libreria import myspgend
from flask_restplus import Resource, Api
mysp=__import__("my-voice-analysis") 
import json
import subprocess
import os
import sys

UPLOAD_FOLDER = './'
ALLOWED_EXTENSIONS = set(['wav'])
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "eWVf+[uZS}^Bl'{"
app.debug = True

def Rango( genero ,frecuencia):
    if(genero == 'hombre'):
        if (frecuencia <= 121.5 and frecuencia >110):
            persona="Hombre Adolecente"
            return persona
        if(frecuencia > 121.95 and frecuencia <=127):
            persona="Hombre Adulto"
            return persona
        #encontrar la relacion
        if(frecuencia > 127.5 and frecuencia < 164):
            persona="Hombre anciano"
            return persona
        elif (frecuencia > 155):
            persona="Niño"
            return persona
    if (genero == 'mujer'):
        if (frecuencia <= 224.58 and frecuencia >196.31):
            persona="Mujer Adolecente"
            return persona
        if(frecuencia <=196.31  and frecuencia >178.92):
            persona="Mujer Adulta"
            return persona
        #encontrar la relacion
        if(frecuencia <= 178.92 ):
            persona="Mujer anciana"
            return persona
        elif (frecuencia > 200):
            persona="Niña "
            return persona


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        print (request.files)
        if 'file' not in request.files:
            return jsonify("Error")
        file = request.files['file']
        if file.filename == '':
            return jsonify("Error")
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            dir_path = str(os.path.dirname(os.path.realpath(__file__)))
            genero=myspgend(filename.strip('.wav'),dir_path)
            frecuencia=mysp.myspf0med(filename.strip('.wav'),dir_path) #asignamos la frecuencia fundamental
            respuesta=Rango(genero,frecuencia)
            return jsonify(respuesta)


app.run(host='0.0.0.0')
