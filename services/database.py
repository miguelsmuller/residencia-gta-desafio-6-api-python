import sqlite3


class MyDatabase:
    def __init__(self) -> None:
        self._db_connection = sqlite3.connect(
            "desafio06.db", check_same_thread=False)
        self._cursor = self._db_connection.cursor()

        create_film_table = "CREATE TABLE IF NOT EXISTS films ( \
            id_film text PRIMARY KEY, \
            title text, \
            synopsis text, \
            genre text, \
            rate text, \
            year text \
        )"
        self._cursor.execute(create_film_table)

        create_series_table = "CREATE TABLE IF NOT EXISTS series ( \
            id_serie text PRIMARY KEY, \
            title text, \
            synopsis text, \
            genre text, \
            rate text, \
            number_seasons text \
        )"
        self._cursor.execute(create_series_table)

        create_episodes_table = "CREATE TABLE IF NOT EXISTS episodes( \
            id_episode text PRIMARY KEY, \
            title text, \
            synopsis text, \
            season text, \
            episode_number, \
            id_serie text, \
            FOREIGN KEY(id_serie) REFERENCES series(id_serie) \
        )"
        self._cursor.execute(create_episodes_table)

        self._db_connection.commit()

    def __del__(self):
        self._db_connection.close()

    #############################
    # FILMS OPERATIONS
    #############################

    def create_film(self, film):
        SQL_command = "INSERT INTO films VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(
            film.id_film,
            film.title,
            film.synopsis,
            film.genre,
            film.rate,
            film.year)

        self._cursor.execute(SQL_command)
        self._db_connection.commit()

    def list_film(self):
        SQL_command = "SELECT * from films;"
        return self._cursor.execute(SQL_command).fetchall()

    def list_film_with_args(self):
        pass

    def find_film(self, id_film):
        SQL_command = "SELECT * FROM films WHERE id_film='{}'".format(
            id_film)
        return self._cursor.execute(SQL_command).fetchone()

    def edit_film(self, film):
        SQL_command = "UPDATE films SET \
            title='{}', \
            synopsis='{}', \
            genre='{}', \
            rate='{}', \
            year='{}' \
            WHERE id_film='{}'".format(
            film.title,
            film.synopsis,
            film.genre,
            film.rate,
            film.year,
            film.id_film
        )

        self._cursor.execute(SQL_command)
        self._db_connection.commit()

    def delete_film(self, film):
        SQL_command = "DELETE FROM films WHERE id_film='{}'".format(
            film.id_film)
        self._cursor.execute(SQL_command)
        self._db_connection.commit()

    #############################
    # SERIES OPERATIONS
    #############################

    def create_serie(self, serie):
        SQL_command = "INSERT INTO series VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(
            serie.id_serie,
            serie.title,
            serie.synopsis,
            serie.genre,
            serie.rate,
            serie.number_seasons
        )

        self._cursor.execute(SQL_command)
        self._db_connection.commit()

    def list_serie(self):
        SQL_command = "SELECT * from series"
        return self._cursor.execute(SQL_command).fetchall()

    def list_serie_with_args(self):
        pass

    def find_serie(self, id_serie):
        SQL_command = "SELECT * FROM series WHERE id_serie='{}'".format(
            id_serie)
        return self._cursor.execute(SQL_command).fetchone()

    def edit_serie(self, serie):
        SQL_command = "UPDATE series SET \
            title='{}', \
            synopsis='{}', \
            genre='{}', \
            rate='{}', \
            number_seasons='{}' \
            WHERE id_serie='{}'".format(
            serie.title,
            serie.synopsis,
            serie.genre,
            serie.rate,
            serie.number_seasons,
            serie.id_serie
        )

        self._cursor.execute(SQL_command)
        self._db_connection.commit()

    def delete_serie(self, serie):
        SQL_command = "DELETE FROM series WHERE id_serie='{}'".format(
            serie.id_serie)
        self._cursor.execute(SQL_command)
        self._db_connection.commit()

    #############################
    # EPISODE OPERATIONS
    #############################
    def create_episode(self, episode):
        SQL_command = "INSERT INTO episodes VALUES ('{}', '{}', '{}', '{}', '{}')".format(
            episode.id_episode,
            episode.title,
            episode.synopsis,
            episode.season,
            episode.id_serie
        )

        self._cursor.execute(SQL_command)
        self._db_connection.commit()

    def list_episode(self, id_episode):
        SQL_command = "SELECT * FROM episodes WHERE id_episode={}".format(
            id_episode)
        return self._cursor.execute(SQL_command).fetchall()

    def list_episode_with_args(self, id_episode):
        pass

    def find_episode(self, id_episode):
        SQL_command = "SELECT * FROM episodes WHERE id_episode='{}'".format(
            id_episode)
        return self._cursor.execute(SQL_command).fetchone()

    def edit_episode(self, media):
        edit_media_SQL = "UPDATE media SET \
            title='{}', \
            synopsis='{}', \
            season='{}', \
            id_serie='{}', \
            WHERE id_episode='{}'".format(
            media.title,
            media.synopsis,
            media.season,
            media.id_serie,
            media.id_episode
        )

        self._cursor.execute(edit_media_SQL)
        self._db_connection.commit()

    def delete_episode(self, serie):
        SQL_command = "DELETE FROM episodes WHERE id_episode='{}'".format(
            serie.id_episode)
        self._cursor.execute(SQL_command)
        self._db_connection.commit()
