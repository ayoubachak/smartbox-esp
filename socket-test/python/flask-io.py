from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def test_connect():
    print('a user connected')

@socketio.on('message')
def handle_message(message):
    print('message: ' + message)
    emit('message', message, broadcast=True)

server_ip = 'localhost'
server_port = 3000

if __name__ == '__main__':
    print(f"Running the server on ws://{server_ip}:{server_port}")
    socketio.run(app, host=server_ip, port=server_port)
