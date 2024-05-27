# creating a Flask app
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


# on the terminal type: curl http://127.0.0.1:5000/ 
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        data = "hello world"
        return jsonify({'data': data})

    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']
        return jsonify({'kredencijali': username + " " + password})


@app.route('/slanje')
def forma():
    return render_template('slanje.html',
                           the_title='Pozdrav!')


@app.route('/home/<int:num>', methods=['GET'])
def disp(num):
    return jsonify({'data': num ** 2})


# driver function
if __name__ == '__main__':
    app.run(debug=True)
