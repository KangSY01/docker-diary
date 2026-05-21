from flask import Flask
import os
import psycopg2

app = Flask(__name__)

DATABASE_URL = os.environ.get('DATABASE_URL')

@app.route('/')
def hello():
    server_id = os.environ.get('SERVER_ID', '1')
    try:
        conn = psycopg2.connect(DATABASE_URL)
        conn.close()
        db_status = 'DB 연결 성공'
    except Exception as e:
        db_status = f'DB 연결 실패: {e}'
    return f'Hello, Diary! I am Server {server_id} / {db_status}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)