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
        return 'This is page 2.'
    return 'You are blocked!'
 
 
@app.route('/page3')
def page3():
    if 'user' in session:
        return 'This is page 3.'
    return 'You are blocked!'


@app.route('/login/<user>')
def login(user: str) -> str:
    session['user'] = True
    return 'You are currently login. '


@app.route('/logout')
def logout() -> str:
    session.pop('user')
    return 'You are currently NOT logged in.'

@app.route('/')
@app.route('/status')
def check_status() -> str:
    if 'user' in session:
        return 'You are currently logged in.'
    return 'You are NOT logged in.'
 
 
if __name__ == '__main__':
    app.run(debug=True)