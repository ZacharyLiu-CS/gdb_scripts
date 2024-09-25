#!/usr/bin/env python3
from flask import Flask, render_template, request
from flask_socketio import SocketIO
import json

app = Flask(__name__)
socketio = SocketIO(app)

# Global list to store coroutine data
coroutine_data = []


@socketio.on('connect')
def handle_connect():
    print("Client connected")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update', methods=['POST'])
def update():
    global coroutine_data
    tasks_info = request.get_json()
    print(f"Received data: {tasks_info}")  # Debug line
    
    # Update the global data list
    coroutine_data.append(tasks_info)
    
    # Emit data to clients

    socketio.emit('update', tasks_info)
    return '', 204  # No Content

@app.route('/data', methods=['GET'])
def get_data():
    return json.dumps(coroutine_data)  # Return current data as JSON


if __name__ == '__main__':
    socketio.run(app, debug=True)

