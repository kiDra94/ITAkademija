# using flask_restful
from flask import Flask, jsonify, request, render_template, make_response, Response
from flask_restful import Resource, Api

# creating the flask app
from flask_restful.representations import json

app = Flask(__name__)
# creating an API object
api = Api(app)

movies = [
    {
        "name": "The Shawshank Redemption",
        "casts": ["Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler"],
        "genres": ["Drama"]
    },
    {
        "name": "The Godfather ",
        "casts": ["Marlon Brando", "Al Pacino", "James Caan", "Diane Keaton"],
        "genres": ["Crime", "Drama"]
    }
]


class Filmovi(Resource):

    # corresponds to the GET request.
    # this function is called whenever there
    # is a GET request for this resource
    def get(self):
        return jsonify(movies)

    # Corresponds to POST request
    def post(self):
        movie = request.get_json()
        movies.append(movie)
        return {'id': len(movies)}, 200


class Film(Resource):
    def get(self, index):
        print(movies[index])
        return jsonify(movies[index])

    def put(self, index):
        movie = request.get_json()
        movies[index] = movie
        #return json.dumps(movies[index]), 200
        return jsonify(movies[index])

    def delete(self, index):
        movies.pop(index)
        return 'None', 200


api.add_resource(Filmovi, '/')
api.add_resource(Film, '/<int:index>')

# driver function
if __name__ == '__main__':
    app.run(debug=True)

'''
Za POST dodati:

{
    "name": "The Dark Knight Updated",
    "casts": ["Christian Bale", "Heath Ledger", "Aaron Eckhart", "Michael Caine"],
    "genres": ["Action", "Crime", "Drama"]
}


Za PUT dodati:

{
    "name": "The Shawshank Redemption 2",
    "casts": ["Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler"],
    "genres": ["Drama"]
}
'''