import time
from json import loads, dumps
from services.database import MyDatabase


class FilmModel:
    database_service: MyDatabase = None

    def __init__(self, title, synopsis, genre, rate, year, id_film=None):
        if id_film:
            self.id_film = id_film
        else:
            self.id_film = round(time.time() * 1000)

        self.title = title
        self.synopsis = synopsis
        self.genre = genre
        self.rate = rate
        self.year = year

    @classmethod
    def find_film(cls, id_film):
        found_film = None
        film = cls.database_service.find_film(id_film)
        print(film)
        if film:
            found_film = FilmModel(
                film[1], film[2], film[3], film[4], film[5], film[0])
        return found_film

    @ classmethod
    def add_film(cls, film):
        cls.database_service.create_film(film)

    @ classmethod
    def remove_film(cls, film):
        cls.database_service.delete_film(film)

    @ classmethod
    def edit_film(cls, film):
        cls.database_service.edit_film(film)

    @ classmethod
    def list_to_dict(cls):
        # return loads(dumps(cls._films_list, default=FilmModel.to_dict))

        result = cls.database_service.list_film()
        film_list = []
        for film in result:
            film_list.append(
                FilmModel(film[1], film[2], film[3], film[4], film[5], film[0]))
        return loads(dumps(film_list, default=FilmModel.to_dict))

    def to_dict(self):
        return {
            "Id": self.id_film,
            "Title": self.title,
            "Synopsis": self.synopsis,
            "Genre": self.genre,
            "Rate": self.rate,
            "Release Year": self.year
        }
