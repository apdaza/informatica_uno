from flask import Flask, render_template, redirect, url_for, request
from modelo.personas import *

app = Flask(__name__)

@app.route("/")
def inicio():
    data = get_all()
    return render_template('listar.html', data = data)

@app.route("/agregar", methods = ['POST', 'GET'])
def agregar():
    if request.method == 'GET':
        return render_template('agregar.html')
    else:
        info = request.form
        data = {
            'nombre': info['nombre'],
            'apellido': info['apellido'],
            'ciudad': info['ciudad']
        }
        add_one(data)
        return redirect(url_for('inicio'))

@app.route("/editar/<id>", methods = ['POST', 'GET'])
def editar(id):
    if request.method == 'GET':
        data = get_one(id)
        return render_template('editar.html', data = data)
    else:
        info = request.form
        data = {
            'nombre': info['nombre'],
            'apellido': info['apellido'],
            'ciudad': info['ciudad']
        }
        update_one(id, data)
        return redirect(url_for('inicio'))

@app.route("/eliminar/<id>")
def eliminar(id):
    delete_one(id)
    return redirect(url_for('inicio'))

if __name__ == '__main__':
    app.run(debug=True)