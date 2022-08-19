from flask import Flask, request
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
def hello():
    file = ''
    data = result(file)
    data = revise(data[0])
    return data    

@app.route('/inference',methods=['POST'])
def inference():
    file = request.files.get('file');
    data = result(file)
    data = revise(data[0])
    return data

if __name__ == '__main__':
    app.run()