from flask import Flask,url_for
app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {username}'

@app.route('/post/<year>/<month>/<day>')
def show_post(year, month, day):  
    return f'Post for {year}/{month}/{day}'

@app.route('/')
def index():
    user_url = url_for('show_user_profile', username='John')
    post_url = url_for('show_post', year='2025', month='10', day='01')
    return f'User URL: {user_url}<br>Post URL: {post_url}'

# test: 1.terminal -> flask run
#       2. browser -> http://127.0.0.1:5000/
