from flask_restx import Resource, Namespace
from models import Movie

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        movies = Movie.query.all()
        return movies, 200

    # def post(self):
    #     return "", 201
