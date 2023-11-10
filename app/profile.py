from app import app , mysql, socketio
from flask import render_template, request, session, url_for, redirect


@app.route('/profile')
def show_profile():
    if 'logged' in session and session['logged']:
        cursor = mysql.connection.cursor()

        sql = "SELECT email FROM users WHERE uid = %s"

        cursor.execute(sql, (session['id'], ))

        name = cursor.fetchone()

        sql = "SELECT nombre, cantidad FROM item INNER JOIN orders ON item.iid = orders.iid WHERE orders.uid = %s"

        cursor.execute(sql, (session['id'], ))

        orders = cursor.fetchall()

        return render_template('pages/profile.html', name = name[0], orders = orders )
    else:
        return redirect(url_for('main_page'))