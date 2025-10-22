## 세션 사용해보기

from flask import Flask, session, abort

app = Flask(__name__)
            
app.secret_key = 'yout_secret_key'  # 세션 데이터를 암호화하기 위한 비밀 키 설정

# 세션 데이터 설정 라우트
@app.route('/set_session')
def set_session():
    session['username'] = 'John'
    return '세션에 사용자 이름이 설정되었습니다.'

# 세션 데이터 가져오기 라우트    
@app.route('/get_session')
def get_session():
    username = session.get('username')
    if username:
        return f'사용자 이름: {username}'
    else:
        return '세션에 사용자 이름이 설정되지 않았습니다.'

# 세션에 'username'이 설정되어 있지 않으면 403 에러 반환
@app.route('/protected')
def protected():
    if 'username' not in session:
        abort (403)
        return '이 페이지는 로그인한 사용자만 접근할 수 있습니다.'
    else:
        return '로그인된 페이지입니다.'
    