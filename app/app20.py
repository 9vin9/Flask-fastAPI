## 쿠키 사용법

from flask import Flask, make_response, request, abort

app = Flask(__name__)

@app.route('/setcookie')
def set_cookie():
    resp = make_response("쿠키를 설정합니다!")
    resp.set_cookie('username', 'John')
    return resp

@app.route('/getcookie')
def get_cookie():
    username = request.cookies.get('username', '게스트')
    return f'쿠키로부터 얻은 사용자 이름: {username}'

# 쿠키가 설정된 사용자만 접근 가능한 라우트
@app.route('/secret')
def secret_page():
    username = request.cookies.get('username')
    if not username:
        abort(403, description="접근 권한이 없습니다. 먼저 쿠키를 설정해주세요.")   # 쿠키가 없으면 403 에러 반환
        return f'환영합니다, {username}님! 비밀 페이지에 접속하셨습니다.'
    
# 응답 객체: resp 가정 시 쿠기 삭제하려면 resp.delete_cookie('cookie_name') 사용
@app.route('/deletecookie')
def delete_cookie():
    resp = make_response("쿠키를 삭제합니다!")
    resp.delete_cookie('username')
    return resp


## 다른 예제

# max_age: 쿠키의 수명을 초 단위로 설정
# resp.set_cookie('username', 'John', max_age=60*60*24*7) # 7일 동안 유효

# expires: 특정 날짜와 시간에 쿠키 만료 설정
# resp.set_cookie('username', 'John', expires=datetime.datetime(2027, 11, 7))   # 2027년 11월 7일에 만료

# path: 쿠키가 유효한 경로 설정
# resp.set_cookie('username', 'John', domain='.example.com')  # example.com 및 하위 도메인에서 유효

# secure: HTTPS 연결에서만 쿠키 전송
# resp.set_cookie('username', 'John', secure=True)

# httponly: 자바스크립트에서 쿠키 접근 방지
# resp.set_cookie('username', 'John', httponly=True)  # True로 설정 시 웹 서버를 통해서만 접근 가능
