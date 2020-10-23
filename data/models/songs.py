from presentation.server import db


class Songs(db.Model):
    song_id = db.Column(db.Integer, primary_key=True, unique=True)
    song_name = db.Column(db.String(250), nullable=False)
    fingerprinted = db.Column(db.SmallInteger)
    file_sha1 = db.Column(db.Binary, unique=True)
    total_hashes = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False)
    date_modified = db.Column(db.DateTime, nullable=False)

    def __init__(self, **kwargs):
        super(Songs, self).__init__(**kwargs)

    @property
    def data_as_dict(self):
        return {
            "song_id": self.song_id,
            "song_name": self.song_name,
            "fingerprinted": self.fingerprinted,
            "file_sha1": self.file_sha1,
            "total_hashes": self.total_hashes,
            "date_created": self.date_created,
            "date_modified": self.date_modified
        }

    def __repr__(self):
        return "User(\n" \
                "\tSong ID: " + str(self.song_id) + "\n" \
                "\tSong name: " + self.song_name + "\n" \
                "\tFingerprinted: " + self.fingerprinted + "\n" \
                "\tFile sha1: " + self.file_sha1 + "\n" \
                "\tTotal hashed: " + self.total_hashes + "\n" \
                "\tDate created: " + self.date_created + "\n" \
                "\tDate modified: " + self.date_modified + "\n" \
                ")"
