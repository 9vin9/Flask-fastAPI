from flask import Flask,url_for
app = Flask(__name__)

# 하드코딩 하지 않고 flask의 url_for 함수를 사용하여 URL을 생성하는 방법

# home page route
@app.route('/')
def index():
    # url_for('index') 호출
    return f'홈페이지 : {url_for("index")}'

# user profile page 
@app.route('/user/<username>')
def user_profile(username):
    return f'{username}의 프로필 페이지: {url_for("user_profile", username=username)}'

# static file route
@app.route('/static-example')
def static_example():
    # url_for ('static', filename='style.css') 호출
    return f'정적 파일 경로: {url_for("static", filename="style.css")}'

# 절대 url test
@app.route('/absolute')
def absolute():
    # url_for('index', _external=True) 호출
    return f'절대 URL: {url_for("index", _external=True)}'

#Http와 절대 url test
@app.route('/https')
def https():
    # url_for('index', _external=True, _scheme='https') 호출
    return f'HTTPS 절대 URL: {url_for("index", _external=True, _scheme="https")}'

#Test: 1. http://127.0.0.1:5000/ -> 홈페이지 url 반환
#      2. http://127.0.0.1:5000/user/john -> john의 프로필 페이지 url 반환
#      3. http://127.0.0.1:5000/static-example -> 정적 파일 경로 반환
#      4. http://127.0.0.1:5000/absolute -> 절대 URL 반환
#      5. http://127.0.0.1:5000/https -> HTTPS 절대 URL 반환