from app import app , mysql, socketio
from flask import render_template, request, session, url_for, redirect

@app.route('/cart')
def show_cart():
    if 'logged' in session and session['logged']:

        cursor = mysql.connection.cursor()

        sql = "SELECT cart.iid, nombre, cantidad  FROM item, cart WHERE uid = %s and cart.iid = item.iid"

        cursor.execute(sql, (session['id'], ))

        results = cursor.fetchall()



        return render_template('pages/cart.html', items = results)

    else:
        return redirect(url_for('main_page'))
    
@app.route('/buy', methods = ['GET', 'POST'])
def buy():
    if request.method == 'POST':
        if 'logged' in session and 'id' in session:
            items = request.form.getlist('item')
            cantidades = request.form.getlist('name')

            for item, cantidad in zip(items, cantidades):
                codigo = item.split("-")
                codigo = codigo[0].strip()

                if cantidad > 0:
                    cursor = mysql.connection.cursor()

                    sql = "INSERT INTO orders (iid, uid, cantidad) VALUES (%s, %s, %s)"

                    cursor.execute(sql, (codigo, session['id'], cantidad, ))

                    mysql.connection.commit()
            
            sql = "DELETE FROM cart WHERE uid = %s"

            cursor.execute(sql, (session['id'], ))

            mysql.connection.commit()

            cursor.close()

            return redirect(url_for('main_page'))

        else:
            return redirect(url_for('main_page'))
    else:
        return redirect(url_for('main_page'))

@app.route('/add-cart', methods = ['POST', 'GET'])
def add_cart():
    if request.method == 'POST':
        if 'logged' in session and 'id' in session:
            
            iid = request.form.get('iid')

            cursor = mysql.connection.cursor()

            sql = "SELECT cantidad FROM cart WHERE iid = %s and uid = %s"

            cursor.execute(sql, (iid, session['id'], ))

            result = cursor.fetchone()

            if result is not None:

                sql = "UPDATE cart SET cantidad = %s WHERE iid = %s and uid = %s"

                cursor.execute(sql, (result[0]+1, iid, session['id'],))

                mysql.connection.commit()

            else:

                sql = "INSERT INTO cart (iid, uid, cantidad) VALUES (%s, %s, %s)"

                cursor.execute(sql, (iid, session['id'], 1, ))

                mysql.connection.commit()

                return redirect(url_for('main_page'))
        else:
            return redirect(url_for('main_page'))
    else:
        return redirect(url_for('main_page'))