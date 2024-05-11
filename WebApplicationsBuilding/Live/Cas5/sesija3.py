from flask import Flask, session
from check_logged_in import check_logged_in
 
app = Flask(__name__)
 
 
@app.route('/')
def hello():
    return 'Hello from the simple webapp.'
 
 
@app.route('/page1')
def page1():
    if check_logged_in():
        return 'You are now logged in.'
    return 'This is page 1.'
 
 
@app.route('/page2')
def page2():
    if check_logged_in():
        return 'You are now logged in.'
    return 'This is page 2.'
 
 
@app.route('/page3')
def page3():
    if check_logged_in():
        return 'You are now logged in.'
    return 'This is page 3.'
 
 
@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in.'
 
 
@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'You are now logged out.'
 
 
@app.route('/status')
def check_status() -> str:
    if check_logged_in():
        return 'You are currently logged in.'
    return 'You are NOT logged in.'
 
 
app.secret_key = 'YouWillNeverGuessMySecretKey'
 
if __name__ == '__main__':
    app.run(debug=True)