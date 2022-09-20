from flask import Flask, render_template, url_for , request, redirect
import requests

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def principal():
    if request.method == 'POST':
        nombre = request.form.get('username', None)
        contrasena = request.form.get('contrasenha', None)
        patronal = request.form.get("patronal", None)
        check= request.form.get("check", None)
        return redirect(url_for('home')) 

    return render_template('login.html')

class clase:
    def __init__(self,img,titulo,desc):
        self.img = img
        self.titulo = titulo
        self.desc = desc
        
@app.route("/home",methods=['GET'])
def home():
    lista_clases = []
    lista_clases.append(clase('clase1.png','Introducción a tallado en madera','''De la mano de nuestro gran artista, llega este curso
con todo lo que necesitas saber para integrarte en 
el hermoso mundo del tallado......'''))
    lista_clases.append(clase('clase2.png','Introducción a tallado en madera','''De la mano de nuestro gran artista, llega este curso
    con todo lo que necesitas saber para integrarte en 
    el hermoso mundo del tallado......'''))
    lista_clases.append(clase('clase3.png','Introducción a tallado en madera','''De la mano de nuestro gran artista, llega este curso
    con todo lo que necesitas saber para integrarte en 
    el hermoso mundo del tallado......'''))
    lista_clases.append(clase('clase4.png','Introducción a tallado en madera','''De la mano de nuestro gran artista, llega este curso
    con todo lo que necesitas saber para integrarte en 
    el hermoso mundo del tallado......'''))
    lista_clases.append(clase('clase5.png','Introducción a tallado en madera','''De la mano de nuestro gran artista, llega este curso
    con todo lo que necesitas saber para integrarte en 
    el hermoso mundo del tallado......'''))
    #cargar mas de la foto de ellos y agregar el texto de figma
    return render_template('index.html',clases=lista_clases)