# creating a Flask app
from flask import Flask, jsonify, request

app = Flask(__name__)


# on the terminal type: curl http://127.0.0.1:5000/ 
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        data = "hello world"
        return jsonify({'data': data})
    
# driver function
if __name__ == '__main__':
    app.run(debug=True)