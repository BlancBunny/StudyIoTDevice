from flask import Flask, render_template, request
from flask.wrappers import Request
from werkzeug.exceptions import RequestedRangeNotSatisfiable

# Flask 객체 인스턴스 생성
app = Flask(__name__)

@app.route('/', methods=('GET', 'POST')) # 최초 접속 URL
def index():
    if request.method == 'GET':
        pass
    
    elif request.method == 'POST':
        userid = request.form.get('userid')
        password = request.form.get('password')

    return render_template('login.html', data={'userid':userid, 'password':password})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)