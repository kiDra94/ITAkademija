from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/user/<username>')
def profile(username):
    return f'Hello, {username}!'


if __name__ == '__main__':
    with app.test_request_context():
        print(url_for('index'))  # Output: '/'
        print(url_for('profile', username='john'))  # Output: '/user/john'
