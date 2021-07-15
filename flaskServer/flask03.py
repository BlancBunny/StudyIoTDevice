from flask import Flask, render_template

# Flask 객체 인스턴스 생성
app = Flask(__name__)

@app.route('/') # 최초 접속 URL
def index():
    return render_template('index.html', user='김현수', data={'userid':'blancbunny95', 'gender':'male', 'age':27})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)