from json import loads, dumps
import time
from services.database import MyDatabase


class SeriesModel:
    database_service: MyDatabase = None

    def __init__(self, title, synopsis, genre, rate, number_seasons, id_serie):
        if id_serie:
            self.id_serie = id_serie
        else:
            self.id_serie = round(time.time() * 1000)
        self.title = title
        self.synopsis = synopsis
        self.genre = genre
        self.rate = rate
        self.number_seasons = number_seasons

    def to_dict(self):
        return {
            "title": self.title,
            "synopsis": self.synopsis,
            "genre": self.genre,
            "rate": self.rate,
            "number_seasons": self.number_seasons,
        }
