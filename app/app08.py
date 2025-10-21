from flask import Flask, request

app = Flask(__name__)

@app.route('/query')
def query_example():
    language = request.args.get('language')
    return f"Requested language: {language}"

# test: 1. terminal -> flask run
#       2. open browser -> http://127.0.0.1:5000/query?language=pyhthon