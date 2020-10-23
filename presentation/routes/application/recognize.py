import os
import json
from flask import Blueprint, render_template, request, flash
from flask_login import current_user
from werkzeug.utils import secure_filename

from dejavu import Dejavu
from dejavu.logic.recognizer.file_recognizer import FileRecognizer
from dejavu.logic.recognizer.microphone_recognizer import MicrophoneRecognizer

from presentation.server import app
from data.utils.validator_file import allowed_file

from bussiness.services.playlist_service import PlaylistService

recognize_bp = Blueprint('recognize_bp', __name__)

playlist_service = PlaylistService()

with open("dejavu.cnf.SAMPLE") as f:
    config = json.load(f)

djv = Dejavu(config)


@recognize_bp.route("/app/recognize", methods=['GET', 'POST'])
def recognize():
    if request.method == "POST":
        if 'file' not in request.files:
            flash('Nu s-a incarcat nicio piesa!', 'danger')
        else:
            file = request.files['file']
            if file.filename == '':
                flash('Nu s-a incarcat nicio piesa!', 'danger')
            elif file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)

                recognizer = FileRecognizer(djv)
                try:
                    results = recognizer.recognize_file(file_path)

                    if results['results'][0]['input_confidence'] > 0.3:
                        list_results = results['results']
                        song_id = list_results[0]["song_id"]
                        song_recognized = list_results[0]['song_name']

                        if current_user.is_authenticated:
                            playlist_service.add(current_user.id, song_id)

                        flash('The result is: {}'.format(song_recognized.decode('utf-8')), 'success')
                    else:
                        flash('The song couldn\'t be recognize', 'danger')
                except Exception as e:
                    print('The song couldn\'t be recognize, error: {}'.format(e))
                    flash('The song couldn\'t be recognize', 'danger')

    return render_template("application/recognize.html")


@recognize_bp.route("/recognize-song-by-mic", methods=["GET"])
def recognize_song_by_mic():
    seconds = request.args['seconds']

    results = djv.recognize(MicrophoneRecognizer, seconds=seconds)

    print (results[0])

    if results[0] and results[0][0]['input_confidence'] >= 0.2:
        songs_recognized = results[0]
        if current_user.is_authenticated:
            playlist_service.add(current_user.id, songs_recognized[0]["song_id"])
        return json.dumps({"song_name": songs_recognized[0]["song_name"].decode("utf-8")}), 200

    return "Song couldn't be recognized", 404
