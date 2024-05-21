# using flask_restful
from flask import Flask, jsonify, request, render_template, make_response, Response
from flask_restful import Resource, Api

app = Flask(__name__)

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

class Obrada(Resource):

    def get(self):
        return jsonify(movies)

    def post(self):
        movie = request.get_json()
        movies.append(movie)
        return {'id': len(movies)-1}, 200

class JedanFilm(Resource):

    def get(self, index):
        return jsonify(movies[index])

api.add_resource(Obrada, '/')
api.add_resource(JedanFilm, '/movies/<int:index>')


# driver function
if __name__ == '__main__':
    app.run(debug=True)