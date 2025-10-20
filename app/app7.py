from flask import Flask

app = Flask(__name__)

@app.route('/int/<int:var>')
def int_type(var):
    return f'Integer: {var}'

@app.route('/float/<float:var>')
def float_var(var: float):
    return f'Float: {var}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath: {subpath}'

@app.route('/uuid/<uuid:some_id>')
def show_uuid(some_id):
    return f'UUID: {some_id}'

#test: 1. terminal -> flask run
#      2. browser -> http://127.0.0.1:5000/int/42
#      3. browser -> http://127.0.0.1:5000/float/3.14
#      4. browser -> http://127.0.0.1:5000/path/hello/world
#      5. browser -> http://127.0.0.1:5000/uuid/123e4567-e89b-12d3-a456-426614174000
