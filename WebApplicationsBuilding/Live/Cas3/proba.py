from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'

@app.route('/proba')
def proba() -> str:
    return 'Hello world from Flask, proba!'

app.run()