from app import app , mysql, socketio
from flask import render_template, request, session, url_for, redirect

@app.route('/cart')
def show_cart():
    if 'logged' in session and session['logged']:
        return render_template('pages/cart.html')
    else:
        return redirect(url_for('main_page'))