from bussiness.repositories.playlist_repository import PlaylistRepository


class PlaylistService:
    def __init__(self):
        self.__playlist_repository = PlaylistRepository()

    def get_all_song_names_by_user_id(self, _user_id):
        return self.__playlist_repository.get_all_song_names_by_user_id(_user_id)

    def add(self, _user_id, _song_id):
        return self.__playlist_repository.add(_user_id, _song_id)
