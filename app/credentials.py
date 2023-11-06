from app import app, mysql
from flask import render_template, request, redirect, url_for, session


app.secret_key = "nuestraClaveSecretaUWU"

@app.route('/login')
def login():
    if 'username' not in session:
        return render_template('pages/login.html')
    else:
        return redirect(url_for('main_page'))

@app.route('/logout')
def log_out():
    if 'username' in session:
        session.pop('username', None)

    if 'id' in session:
        session.pop('id', None)

    if 'logged' in session:
        session.pop('logged', None)

    return redirect(url_for('main_page'))

@app.route('/register')
def register():
    if 'username' not in session:
        return render_template('pages/register.html')
    else:
        return redirect(url_for('main_page'))

@app.route('/iniciar', methods = ['GET', 'POST'])
def iniciar():
    if 'username' not in session:
        if request.method == 'POST':
            user = request.form.get('user') 
            password = request.form.get('password')

            cursor = mysql.connection.cursor()

            cursor.execute('SELECT * FROM users WHERE email LIKE %s AND password LIKE %s;', (user, password,))
           
            results = cursor.fetchall()
            
            cursor.close()
            
            if len(results) > 0:

                session['username'] = user

                session['logged'] = True

                session['id'] = results[0][0] 

                return redirect(url_for('main_page'))

            else:

                return redirect(url_for('login'))


    else:
        return redirect(url_for('main_page'))
    

@app.route('/registrar', methods = ['GET', 'POST'])
def registar_usuario():
    if request.method == 'POST':
        email =  request.form.get('user')
        password = request.form.get('password')
        
        cursor = mysql.connection.cursor()

        cursor.execute('SELECT * FROM users WHERE email = %s', (email, ))

        results = cursor.fetchall()
        if len(results) > 0:
            cursor.close()
            return redirect(url_for('register'))
        else:
            cursor.execute('INSERT INTO users (email, password) VALUES (%s, %s)', (email, password,))
            mysql.connection.commit()

            cursor.close()
    
            return redirect(url_for('main_page')) 

