from app import app , mysql, socketio
from flask import render_template, request, session, url_for, redirect
from flask_socketio import send

@socketio.on('message')
def handle_message(message):
    print("Received message: " + message)
    if message != "User connected!": 
        send(message, broadcast=True)

@app.route('/chat')
def show_chat():
    return render_template('pages/chat.html')
