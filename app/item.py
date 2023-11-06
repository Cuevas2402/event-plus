from app import app, mysql
from flask import render_template, request, redirect, url_for, session, jsonify

@app.route('/details/<id>')
def show_item(id):
    if id is not None:
        cursor = mysql.connection.cursor()
        sql = "SELECT nombre, tipo, img, desc_g FROM item WHERE iid = %s;"

        cursor.execute(sql, (id, ))

        result = cursor.fetchone()

        return render_template('pages/item.html', item = result)
    else:
        return redirect(url_for('main_page'))



