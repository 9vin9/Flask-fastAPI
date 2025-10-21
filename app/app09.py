from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/json')
def json_example():
    # jsonfiy() 함수를 사용하여 JSON 응답 반환
    return jsonify({"message": "Hell0, World!"})

# test: 1. terminal -> flask run
#       2. open browser -> http://127.0.0.1:5000/json