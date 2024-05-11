from flask import Flask, session

app = Flask(__name__)

app.secret_key = 'YouWillNeverGuess'

@app.route('/')
def hello():
    return 'Hello from the simple webapp.'


@app.route('/page1')
def page1():
    if 'user' in session:
        return 'This is page 1.'
    return 'You are blocked!'


@app.route('/page2')
def page2():
    if 'user' in session:
        return 'This is page 1.'
    return 'You are blocked!'


@app.route('/page3')
def page3():
    if 'user' in session:
        return 'This is page 1.'
    return 'You are blocked!'


@app.route('/login/<user>')
def login(user: str) -> str:
    session['user'] = True 
    return 'User are currently logged in!'


@app.route('/status')
def check_status() -> str:
    if 'user' in session:
        return 'Status: You are currently logged in.'
    return 'Status: You are NOT logged in.'

@app.route('/logout')
def dlogout() -> str:
    session.pop('user')
    return 'Logout: You are currently NOT logged in.'

if __name__ == '__main__':
    app.run(debug=True)
