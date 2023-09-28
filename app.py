from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_wtf import FlaskForm
from wtforms import StringField
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

t = 0
num_clients = 0
list_of_words = []

class User:
    def __init__(self, time):
        self.time = time

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
    global t
    time.sleep(1)
    print(f'received message: {message}')
    socketio.send(t)
    t += 1

@socketio.on('connect')
def handle_connect():
    global num_clients
    num_clients += 1
    emit('update_count', num_clients, broadcast=True)

@socketio.on('disconnect')
def handle_disconnect():
    global num_clients
    num_clients -= 1
    emit('update_count', num_clients, broadcast=True)

    
if __name__ == '__main__':
    socketio.run(app)