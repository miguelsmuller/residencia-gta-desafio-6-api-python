from flask import Flask
from flask_restful import Api

from services.database import MyDatabase

from resources.filmRoutes import Film
from resources.seriesRoutes import Series

from model.episodes import EpisodesModel
from model.films import FilmModel
from model.series import SeriesModel

app = Flask(__name__)
api = Api(app)

database = MyDatabase()

EpisodesModel.database_service = database
FilmModel.database_service = database
SeriesModel.database_service = database

api.add_resource(Film, "/films/<int:id_film>", "/films")
api.add_resource(Series, "/series/<int:id_serie>", "/series")

if __name__ == '__main__':
    app.run(debug=True)
