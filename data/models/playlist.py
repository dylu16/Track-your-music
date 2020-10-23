from presentation.server import db


class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    user_id = db.Column(db.Integer, nullable=False)
    song_id = db.Column(db.Integer, nullable=False)

    def __init__(self, **kwargs):
        super(Playlist, self).__init__(**kwargs)

    @property
    def data_as_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "song_id": self.song_id
        }

    def __repr__(self):
        return "User(\n" \
                "\tID: " + str(self.id) + "\n" \
                "\tUser ID: " + str(self.user_id) + "\n" \
                "\tSong ID: " + str(self.song_id) + "\n" \
                ")"
