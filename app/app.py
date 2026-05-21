from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    server_id = os.environ.get('SERVER_ID', '1')
    return f'Hello, Diary! I am Server {server_id}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)