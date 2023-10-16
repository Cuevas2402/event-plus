from app import app, mysql
from flask import render_template, request, redirect, url_for, session, jsonify

@app.route('/filter', methods = ['GET', 'POST'])
def filters():
    if request.method == 'POST':
        data = {}
        data['categoria'] = request.form.get('categoria')
        data['precio'] = request.form.get('precio')
        data['calificacion'] = request.form.get('calificacion')
        data['ubicacion'] = request.form.get('ubicacion')
        data['fecha'] = request.form.get('fecha')

        condiciones = []

        if data['categoria']:
            condiciones.append("tipo LIKE '{}'".format(data['categoria']))
        if data['precio']:
            condiciones.append("precio BETWEEN 0.00 AND {}.00 ".format(data['precio']))
        if data['calificacion']:
            condiciones.append("calificacion = {}".format(data['calificacion']))
        if data['ubicacion']:
            condiciones.append("ubicacion = {}".format(data['ubicacion']))
        if data['fecha']:
            condiciones.append("fecha = {}".format(data['fecha']))

        condicion_sql = " OR ".join(condiciones)

        sql = f"SELECT iid, nombre, desc_p, img FROM item WHERE {condicion_sql};"

        cursor = mysql.connection.cursor()
        
        cursor.execute(sql)

        results = cursor.fetchall()

        htmls = []

        for result in results:
            htmls.append(render_template('/components/card.html', id = result[0], titulo = result[1], descripcion = result[2], imagen = result[3] ))
        return jsonify(htmls = htmls) 
