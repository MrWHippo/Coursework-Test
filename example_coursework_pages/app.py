from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class LoginForm(FlaskForm):
    username = StringField("username")
    password = PasswordField("password")
    submit = SubmitField("submit")

class RegisterForm(FlaskForm):
    username = StringField("username")
    password = PasswordField("password")
    submit = SubmitField("submit")

class ChangePassword(FlaskForm):
    password = PasswordField("password")
    submit = SubmitField("Submit")

class ChangeUsername(FlaskForm):
    username = StringField("username")
    submit = SubmitField("Submit")


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.is_submitted():
        username = form.username.data
        password = form.password.data
        return render_template('home.html')
    else:
        return render_template('login.html',form=form)

@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.is_submitted():
        username = form.username.data
        password = form.password.data
        return render_template('home.html')
    else:
        return render_template('register.html',form=form)

@app.route('/', methods=["GET", "POST"])
def home():
    return render_template('home.html')

@app.route('/leaderboard')
def leaderboard():
    return render_template('leaderboard.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')

@app.route('/account')
def account():
    password_form = ChangePassword()
    username_form = ChangeUsername()
    
    return render_template('account.html')

@app.route('/aiGame')
def aiGame():
    return render_template('game_ai.html')

@app.route('/hotseatGame')
def hotseatGame():
    return render_template('game_hs.html')
