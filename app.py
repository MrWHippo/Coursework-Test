from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, join_room, leave_room, send
from flask_wtf import FlaskForm
from wtforms import StringField
import time
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
clients = {}

t = 0
num_clients = 0
client_num = 0
list_of_words = []

class User:
    def __init__(self, id, client_num, time):
        self.id = id
        self.time = time
        self.cleint_num = client_num
        self.last_update = datetime.now()

    def increase_time(self):
        self.time += 1
    
    #(datetime.now() + timedelta(seconds=1)
     
    def time_has_been_changed(self):
        print(self.last_update)
        print("Current T : ",datetime.now())
        if self.last_update + timedelta(seconds=1) <= datetime.now():
            return False
        else:
            return True

class Word_Entry(FlaskForm):
    word = StringField("word_input")

def send_word(word):
    global list_of_words
    list_of_words.append[word]
    emit('new_word', list_of_words, broadcast=True)

@app.route('/', methods=["GET", "POST"])
def index():
    form = Word_Entry()
    print("site entered")
    if form.is_submitted():
        word = form.word.data
        return render_template('index2.html', form =form)
    return render_template('index2.html', form=form)

@socketio.on('message')
def handle_message(message):
    user_id = request.sid
    user = clients[user_id]
    time.sleep(1)
    print(f'received message: {message}')
    socketio.send(user.time)
    if user.time_has_been_changed() == False:
        user.increase_time()

@socketio.on('connect')
def handle_connect(data):
    global num_clients, clients, client_num
    num_clients += 1
    client_num += 1
    client_id = request.sid
    time = 0
    client = User(client_id, client_num, time)
    clients[client.id] = client
    emit('update_count', num_clients, broadcast=True)

@socketio.on('disconnect')
def handle_disconnect(data):
    global num_clients
    num_clients -= 1
    emit('update_count', num_clients, broadcast=True)

@socketio.on('join_room')
def on_join_room(data):
    username = data['username']
    room = data['room']
    join_room(room)
    send(username + 'has entered the room.', to=room)

@socketio.on('leave_room')
def on_leave_room(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    send(username + ' has left the room.', to=room)
    
if __name__ == '__main__':
    socketio.run(app)