# # server.py
# from flask import Flask, render_template
# from flask_socketio import SocketIO, emit
# import cv2
# import base64

# app = Flask(__name__)
# socketio = SocketIO(app)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @socketio.on('video_frame')
# def handle_video_frame(data):
#     # Broadcast the received frame to all connected clients
#     emit('broadcast_frame', data, broadcast=True)

# if __name__ == '__main__':
#     socketio.run(app, debug=True)



# from flask import Flask, render_template
# from flask_socketio import SocketIO, emit

# app = Flask(__name__)
# socketio = SocketIO(app)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @socketio.on('new_user')
# def handle_new_user(data):
#     # Broadcast the new user's box color to all connected clients
#     emit('new_user_box', data, broadcast=True)

# if __name__ == '__main__':
#     socketio.run(app, debug=True)


# from flask import Flask, render_template
# from flask_socketio import SocketIO, emit

# app = Flask(__name__)
# socketio = SocketIO(app)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @socketio.on('new_user')
# def handle_new_user(data):
#     # Broadcast the new user's image to all connected clients
#     emit('new_user_image', data, broadcast=True)

# if __name__ == '__main__':
#     socketio.run(app, debug=True)

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('image_capture')
def handle_image_capture(data):
    # Broadcast the received image to all connected clients
    emit('broadcast_image', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=false,host='0.0.0.0')
