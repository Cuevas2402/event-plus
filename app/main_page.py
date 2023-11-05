from app import app, mysql
from flask import render_template, redirect, url_for

@app.route('/')
def main_page():
    cursor = mysql.connection.cursor()

    sql = 'SELECT iid, nombre, desc_p, img FROM item;'

    cursor.execute(sql)

    results = cursor.fetchall()
    htmls = []
    for result in results:
        htmls.append(render_template('/components/card.html', id = result[0], titulo = result[1], descripcion = result[2], imagen = result[3] ))
    return render_template('pages/index.html', htmls = htmls)

@app.errorhandler(404)
def not_found(err):
    return redirect(url_for('main_page'))