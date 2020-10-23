from presentation.server import db
from data.models.playlist import Playlist
from data.models.songs import Songs


class PlaylistRepository:
    def __init__(self):
        self.__db_context = db.session

    def add(self, _user_id, _song_id):
        playlist = Playlist(
            user_id=_user_id,
            song_id=_song_id
        )
        self.__db_context.add(playlist)
        self.__db_context.commit()

    def get_all_song_names_by_user_id(self, _user_id):
        return self.__db_context.query(Songs.song_name). \
            filter(Playlist.user_id == _user_id). \
            filter(Playlist.song_id == Songs.song_id).all()
