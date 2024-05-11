from flask import Flask, session

app = Flask(__name__)

app.secret_key = 'YouWillNeverGuess'

@app.route('/setuser/<user>')
def setuser(user: str) -> str:
    session['user'] = user
    return 'User value set to: ' + session['user']

@app.route('/getuser')
def getuser() -> str:
    if 'user' in session:
        return 'GetUser: User value is currently set to: ' + session['user']
    return 'GetUser: You are currently NOT logged IN.'

@app.route('/')
@app.route('/status')
def check_status() -> str:
    if 'user' in session:
        return 'Status: You are currently logged in.'
    return 'Status: You are NOT logged in.'

@app.route('/logout')
def logout() -> str:
    session.pop('user')
    return 'Logout: You are currently NOT logged in.'



if __name__ == '__main__':
    app.run(debug=True)
