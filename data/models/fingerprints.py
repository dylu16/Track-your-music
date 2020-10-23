from presentation.server import db


class Fingerprints(db.Model):
    __table_args__ = (
        db.PrimaryKeyConstraint('hash', 'song_id', 'offset'),
    )

    hash = db.Column(db.Binary, nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey("songs.song_id"), nullable=False)
    offset = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False)
    date_modified = db.Column(db.DateTime, nullable=False)

    def __init__(self, **kwargs):
        super(Fingerprints, self).__init__(**kwargs)
