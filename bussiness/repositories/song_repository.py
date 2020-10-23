from presentation.server import db
from data.models.songs import Songs
from sqlalchemy import func


class SongsRepository:
    def __init__(self):
        self.__db_context = db.session

    def get_all(self):
        return self.__db_context.query(Songs).all()

    def get_filtered_songs(self, _string):
        if _string:
            return self.__db_context.query(Songs).filter(func.lower(Songs.song_name).like("%" + _string + "%")).all()
        else:
            return self.__db_context.query(Songs).all()

    def delete_by_id(self, _id):
        try:
            self.__db_context.query(Songs).filter(Songs.song_id == _id).delete()
            self.__db_context.commit()
            return True
        except Exception as e:
            print("Exception occurred on song delete by id: {}".format(e))
            return False
