from flask import Flask
app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {username}'

# test: 1. terminal: export FLASK_APP=app.py
# test: 2. terminal: flask run
# test: 3. open browser: http://127.0.0.1:5000/user/flask_variable_name

