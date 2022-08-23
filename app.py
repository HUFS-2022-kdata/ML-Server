from flask import Flask, request, jsonify
from pydub import AudioSegment
from inference import result
import config

def revise(sentence):
    words = sentence.split()
    result = []
    for word in words:
        tmp = ''    
        for t in word:
            if not tmp:
                tmp += t
            elif tmp[-1]!= t:
                tmp += t
        result.append(tmp)
    return ' '.join(result)

app = Flask(__name__)

@app.route('/')
def start():
    return 'start' 

@app.route('/upload',methods=['POST'])
def inference():
    if request.method == "POST":
        audiofile = request.files["file"]
        filename = audiofile.filename

        track = AudioSegment.from_file(audiofile,  format= 'm4a')
        file_handle = track.export('audio.wav', format='wav')
        response = {}
        data = revise(result()[0])
        response['text'] = data
        print(data)
        
    return jsonify(response)

if __name__ == '__main__':
    app.run(host=config.IP_CONFIG['host'],port='5000')