from app import app, mysql
from flask import render_template, request

@app.route('/login')
def login():
    return render_template('pages/login.html')

@app.route('/register')
def register():
    return render_template('pages/register.html')

#@app.route('/iniciar')
#def iniciar():

@app.route('/registrar', methods = ['GET', 'POST'])
def registar_usuario():
    if request.method == 'POST':
        email =  request.form.get('user')
        password = request.form.get('password')
        
        cursor = mysql.connection.cursor()

        cursor.execute('INSERT INTO users (email, password) VALUES (%s, %s,)', (email, password,))
        mysql.connection.commit()

        return render_template('index.html')
