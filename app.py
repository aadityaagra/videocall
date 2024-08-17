from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('button_clicked')
def handle_button_click():
    emit('display_message', 'Hello')

if __name__ == '__main__':
    socketio.run(app,debug=True)
