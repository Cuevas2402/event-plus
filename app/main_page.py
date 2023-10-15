from app import app, mysql
from flask import render_template

@app.route('/')
def main_page():
    return render_template('pages/index.html')