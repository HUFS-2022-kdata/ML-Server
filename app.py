from flask import Flask
from inference import result

app = Flask(__name__)

data = result()
data = data[0]

@app.route('/')
def hello():
    return data

if __name__ == '__main__':
    app.run()