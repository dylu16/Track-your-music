import json

from dejavu import Dejavu
from dejavu.logic.recognizer.file_recognizer import FileRecognizer
from dejavu.logic.recognizer.microphone_recognizer import MicrophoneRecognizer

# load config from a JSON file (or anything outputting a python dictionary)
with open("dejavu.cnf.SAMPLE") as f:
    config = json.load(f)

if __name__ == '__main__':

    # create a Dejavu instance
    djv = Dejavu(config)

    # Fingerprint all the mp3's in the directory we give it **
    djv.fingerprint_directory("mp3", [".mp3"])

    # Recognize audio from a file
    # results = djv.recognize(FileRecognizer, "mp3/Sean-Fournier--Falling-For-You.mp3")
    # print(f"From file we recognized: {results}\n")

    # # Or recognize audio from your microphone for `secs` seconds
    # secs = 10
    # results = djv.recognize(MicrophoneRecognizer, seconds=secs)
    # if results is None:
    #     print("Nothing recognized -- did you play the song out loud so your mic could hear it? :)")
    # else:
    #     print(f"From mic with {secs} seconds we recognized: {results}\n")

    # Or use a recognizer without the shortcut, in anyway you would like
    # recognizer = FileRecognizer(djv)
    # results = recognizer.recognize_file("piesa.mp3")
    # print(f"No shortcut, we recognized: {results}\n")
