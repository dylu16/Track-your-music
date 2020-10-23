from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required
from bussiness.services.playlist_service import PlaylistService

playlist_service = PlaylistService()

my_playlist_bp = Blueprint('my_playlist_bp', __name__)


@my_playlist_bp.route("/app/my-playlist")
@login_required
def my_playlist():
    if current_user.is_admin:
        return redirect(url_for('recognize_bp.recognize'))

    playlist_songs = playlist_service.get_all_song_names_by_user_id(current_user.id)

    playlist_songs = [song[0] for song in playlist_songs]

    return render_template("application/my_playlist.html", playlist_songs=playlist_songs)
