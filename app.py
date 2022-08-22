from flask import Flask, request
from werkzeug.utils import secure_filename
from inference import result

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
        audiofile.save(secure_filename(audiofile.filename))
    return result(audiofile)

if __name__ == '__main__':
    app.run()