from model.films import FilmModel
from flask_restful import Resource, reqparse


class Film (Resource):
    def post(self):
        body_arguments = reqparse.RequestParser()
        body_arguments.add_argument("title")
        body_arguments.add_argument("synopsis")
        body_arguments.add_argument("genre")
        body_arguments.add_argument("rate")
        body_arguments.add_argument("year")

        params = body_arguments.parse_args()

        new_film = FilmModel(
            params["title"],
            params["synopsis"],
            params["genre"],
            params["rate"],
            params["year"],
        )

        FilmModel.add_film(new_film)
        return new_film.to_dict()

    def get(self, id_film=None):
        if id_film:
            found_film = FilmModel.find_film(id_film)
            if found_film:
                return found_film.to_dict()
            return {"message": "Film not found"}, 404
        else:
            return FilmModel.list_to_dict()

    def delete(self, id_film):
        found_film = FilmModel.find_film(id_film)
        if found_film:
            FilmModel.remove_film(found_film)
            return found_film.to_dict()
        return {"message": "Film not found"}, 404

    def put(self, id_film):
        found_film = FilmModel.find_film(id_film)
        if found_film:
            body_arguments = reqparse.RequestParser()
            body_arguments.add_argument("title")
            body_arguments.add_argument("synopsis")
            body_arguments.add_argument("genre")
            body_arguments.add_argument("rate")
            body_arguments.add_argument("year")

            params = body_arguments.parse_args()

            found_film.title = params.title
            found_film.synopsis = params.synopsis
            found_film.genre = params.genre
            found_film.rate = params.rate
            found_film.year = params.year

            FilmModel.edit_film(found_film)
            return found_film.to_dict()
        return {"message": "Post not found"}, 404
