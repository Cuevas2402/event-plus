from app import app, mysql
from flask import render_template, request, redirect, url_for, session

#@app.route('/filter', methods = ['GET', 'POST'])
#def filters():
#    if request.method == 'POST':
