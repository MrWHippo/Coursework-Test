from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    print("site entered")
    return render_template('index.html')

@socketio.on('connect')
def test_connect(auth):
    print('Connection')
    emit('my response', {'data': 'Connected'})

@socketio.on('message')
def handle_message(data):
    print('received message: data')
    send(data)
    some_function()

@socketio.on('my event')
def handle_my_custom_event(data):
    emit('my response', data, broadcast=True)

def some_function():
    socketio.emit('some event', {'data': 42})
    
if __name__ == '__main__':
    socketio.run(app)