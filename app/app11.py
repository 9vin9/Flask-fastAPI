from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)

# test: 1. terminal -> flask run
#       2. open browser -> http://127.0.0.1/5000/hello/이름

# app.py 파일과 같은 레벨로 templates 폴더