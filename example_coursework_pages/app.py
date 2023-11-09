from flask import Flask, render_template, session
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
        print("form submitted")
        username = form.username.data
        password = form.password.data
        if username == None or password == None:
            return render_template('login.html', form=form)
        else:
            # check username is not already taken
            session["username"] = username
            return render_template('home.html')
    else:
        return render_template('login.html', form=form)


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.is_submitted():
        username = form.username.data
        password = form.password.data
        if username == None or password == None:
            return render_template('register.html', form=form)
        else:
            # check username is not already taken
            session["username"] = username
            return render_template('home.html')
    else:
        return render_template('register.html',form=form)


@app.route('/', methods=["GET", "POST"])
def home():
    username = session.get("username", None)
    if username is not None:
        return render_template('home.html')
    else:
        return render_template('login.html', form=LoginForm)
    

@app.route('/leaderboard')
def leaderboard():
    username = session.get("username", None)
    if username is not None:
        return render_template('leaderboard.html')
    else:
        return render_template('login.html', form=LoginForm)


@app.route('/logout')
def logout():
    try:
        del session["username"]
    except:
        pass
    return render_template('logout.html')


@app.route('/account')
def account():
    username = session.get("username", None)
    if username is not None:
        password_form = ChangePassword()
        username_form = ChangeUsername()
        if password_form.is_submitted():
            return render_template('account.html', form1=ChangePassword, form2=ChangeUsername)
        
        elif username_form.is_submitted():
            return render_template('account.html', form1=ChangePassword, form2=ChangeUsername)
        
        else:
            return render_template('account.html', form1=ChangePassword, form2=ChangeUsername)
    else:
        return render_template('login.html', form=LoginForm)


@app.route('/aiGame')
def aiGame():
    username = session.get("username", None)
    if username is not None:
        return render_template('game_ai.html')
    else:
        return render_template('login.html', form=LoginForm)


@app.route('/hotseatGame')
def hotseatGame():
    username = session.get("username", None)
    if username is not None:
        return render_template('game_hs.html')
    else:
        return render_template('login.html', form=LoginForm)
