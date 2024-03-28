from flask import Flask
import subprocess
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/get_link')
def get_link():
    result = subprocess.run(['python', 'get_link.py'], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

@app.route('/get_mirror')
def get_mirror():
    result = subprocess.run(['python', 'get_mirror.py'], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

@app.route('/get_translators')
def get_translators():
    result = subprocess.run(['python', 'get_translators.py'], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
