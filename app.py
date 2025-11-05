from flask import Flask, render_template, request, redirect
import sqlite3
import webbrowser
app = Flask(__name__)

# Crear tabla si no existe
def init_db():
    conn = sqlite3.connect('adopcion.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS solicitudes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT NOT NULL,
            telefono TEXT NOT NULL,
            motivo TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    nombre = request.form['nombre']
    email = request.form['email']
    telefono = request.form['telefono']
    motivo = request.form['motivo']

    conn = sqlite3.connect('adopcion.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO solicitudes (nombre, email, telefono, motivo)
        VALUES (?, ?, ?, ?)
    ''', (nombre, email, telefono, motivo))
    conn.commit()
    conn.close()

    return redirect('/gracias')

@app.route('/gracias')
def gracias():
    return render_template('gracias.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/imagenes')
def imagenes():
    return render_template('imagenes.html')
if __name__ == '__main__':
    app.run(debug=True)