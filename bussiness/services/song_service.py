from bussiness.repositories.song_repository import SongsRepository


class SongService:
    def __init__(self):
        self.__song_repository = SongsRepository()

    def get_all(self):
        return self.__song_repository.get_all()

    def get_filtered_songs(self, _string):
        return self.__song_repository.get_filtered_songs(_string)

    def detele_by_id(self, _id):
        return self.__song_repository.delete_by_id(_id)
