from flask_restful import Resource, reqparse
from model.series import SeriesModel


class Series(Resource):
    def get(self, id=None):
        if id:
            found_serie = SeriesModel.find_serie(id)
            if found_serie:
                return found_serie.to_dict()
            return {"message": "Serie not found"}, 404
        else:
            return SeriesModel.list_to_dict()

    def post(self):
        body_arguments = reqparse.RequestParser()

        body_arguments.add_argument("title")
        body_arguments.add_argument("synopsis")
        body_arguments.add_argument("genre")
        body_arguments.add_argument("rate")
        body_arguments.add_argument("year")
        body_arguments.add_argument("number_seasons")
        body_arguments.add_argument("episodes", action="append")

        params = body_arguments.parse_args()

        new_serie = SeriesModel
        (
            params["title"],
            params["synopsis"],
            params["genre"],
            params["rate"],
            params["year"],
            params["number_seasons"],
            params["episodes"]
        )

        SeriesModel.add_serie(new_serie)
        return new_serie.to_dict()

    def delete(self, id):
        found_serie = SeriesModel.find_serie(id)
        if found_serie:
            SeriesModel.remove_serie(found_serie)
            return found_serie.to_dict()
        return {"message": "Serie not found"}, 404

    def put(self, id):
        found_serie = SeriesModel.find_serie(id)
        if found_serie:
            body_arguments = reqparse.RequestParser()

        body_arguments.add_argument("title")
        body_arguments.add_argument("synopsis")
        body_arguments.add_argument("genre")
        body_arguments.add_argument("rate")
        body_arguments.add_argument("year")
        body_arguments.add_argument("number_seasons")
        body_arguments.add_argument("episodes")

        params = body_arguments.parse_args()
        found_serie.content = params.text
        SeriesModel.edit_serie(found_serie)
        return found_serie.to_dict()
        return {"message": "Serie not found"}, 404
