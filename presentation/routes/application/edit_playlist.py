import os
import json
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename

from presentation.server import app
from data.forms.upload_song_form import UploadSongForm
from data.utils.validator_file import allowed_file
from data.utils.edit_playlist import convert_to_lower_and_underscore
from bussiness.services.song_service import SongService

from dejavu import Dejavu

song_service = SongService()

edit_playlist_bp = Blueprint('edit_playlist_bp', __name__)

with open("dejavu.cnf.SAMPLE") as f:
    config = json.load(f)

djv = Dejavu(config)


@edit_playlist_bp.route('/app/edit-playlist', methods=["POST", "GET"])
@login_required
def edit_playlist():
    if not current_user.is_admin:
        return redirect(url_for('recognize_bp.recognize'))

    form = UploadSongForm()

    if request.method == "POST":
        if 'upload_song' not in request.files:
            flash('Nu s-a incarcat nicio piesa!', 'danger')
        else:
            file = request.files['upload_song']
            if file.filename == '':
                flash('Nu s-a incarcat nicio piesa!', 'danger')
            elif file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)

                result_fingerprint = djv.fingerprint_file(file_path)

                flash(result_fingerprint, 'success')

    return render_template("application/edit_playlist.html", form=form)


@edit_playlist_bp.route('/app/load-data-playlist')
@login_required
def load_playlist_data():
    if not current_user.is_admin:
        return redirect(url_for('recognize_bp.recognize'))

    draw = int(request.args["draw"])
    start_record_idx = int(request.args["start"])
    records_per_page = int(request.args["length"])
    sort_type = request.args["order[0][dir]"]
    sort_column = request.args["columns[" + request.args["order[0][column]"] + "][name]"]
    search_input = request.args["search[value]"].strip().lower()

    all_songs = song_service.get_all()

    filtered_songs = song_service.get_filtered_songs(search_input)

    len_filtered_songs = len(filtered_songs)

    filtered_songs = filtered_songs[start_record_idx: start_record_idx + records_per_page]

    list_songs = []

    for song in filtered_songs:
        song_as_dict = song.data_as_dict

        song_as_dict["date_created"] = str(song_as_dict["date_created"]).split()[0]
        song_as_dict["date_modified"] = str(song_as_dict["date_modified"]).split()[0]

        list_songs.append(song_as_dict)

    list_songs = sorted(list_songs,
                        key=lambda song_dict: song_dict[convert_to_lower_and_underscore(sort_column)],
                        reverse=True if sort_type == "desc" else False)

    return json.dumps({
        "draw": draw,
        "recordsFiltered": len_filtered_songs,
        "recordsTotal": len(all_songs),
        "data": list_songs
    },
        default=str
    )


@edit_playlist_bp.route('/app/remove-song/<int:song_id>', methods=["DELETE"])
@login_required
def remove_song(song_id):
    if not current_user.is_admin:
        return redirect(url_for('recognize_bp.recognize'))

    if song_service.detele_by_id(song_id):
        djv.refresh()
        return "Success", 200
    else:
        return "Error", 500
