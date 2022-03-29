from json import loads, dumps
import time
from services.database import MyDatabase


class EpisodesModel:
    database_service: MyDatabase = None

    def __init__(self, title, synopsis, season, id_serie, episode_number, id_episode):
        if id_episode:
            self.id_episode = id_episode
        else:
            self.id_episode = round(time.time() * 1000)
        self.title = title
        self.synopsis = synopsis
        self.season = season
        self.episode_number = episode_number
        self.id_serie = id_serie

    def to_dict(self):
        return {
            "title": self.title,
            "synopsis": self.synopsis,
            "season": self.season,
            "id_serie": self.id_serie,
            "episode_number": self.episode_number
        }
