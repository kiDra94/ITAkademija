# using flask_restful
from flask import Flask, jsonify, request, render_template, make_response, Response
from flask_restful import Resource, Api

# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)

# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
# other methods include put, delete, etc.
class Hello(Resource):

    # corresponds to the GET request.
    # this function is called whenever there
    # is a GET request for this resource
    def get(self):
        return jsonify({'message': 'hello world'})

    # Corresponds to POST request
    def post(self):
        data = request.get_json()  # status code
        return jsonify({'data': data}), 201
    
class Square(Resource):

    def get(self, num): 
        return jsonify({'square': num ** 2})   
    
class Faktorijal(Resource):

    def get(slef, num):
        return jsonify({'faktorijal': slef.fakt(num)})
    
    def fakt(self, num):
        pom = 1
        for i in range(2, num+1): # ne smije od 0 posto ce stalnod a mnozi sa 0; 1 se moze preskociti posto 1*1 = 1
            pom *=i
        return pom

class Slanje(Resource):
 
    def get(self):
        #return jsonify({'message': 'Poslato'})
        return make_response(render_template('slanje2.html', the_title='Pozdrav!'))
 
    def post(self):
        username = request.form['email']
        password = request.form['password']
        return jsonify({'kredencijali': username + " " + password})

api.add_resource(Hello, '/')
api.add_resource(Slanje, '/slanje')
api.add_resource(Square, '/square/<int:num>')
api.add_resource(Faktorijal, '/fakt/<int:num>')

# driver function
if __name__ == '__main__':
    app.run(debug=True)