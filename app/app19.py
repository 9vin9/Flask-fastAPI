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
    
    
# 1. 세선 데이터 저장
#   session['user_id'] = 42
#   사용자의 ID를 세션에 저장. 이 ID는 로그인 시 할당된 고유값 일 수 있음

# 2. 세션 데이터 조회
#   user_id = session.get('user_id')
#   세션에서 'user_id' 조회 (값을 가져옴). 값이 없으면 None

# 3. 세션 데이터 삭제
#   session.pop('user_id', None)
#   세션에서 'user_id' 키를 가진 세션 데이터 삭제. 두 번째 인자는 키가 없을 때 반환할 기본값

# 4. 세션 데이터의 존재 여부 확인
#   is_logged_in = 'user_id' in session
#   세션에 'user_id' 키가 존재하는지 확인 (로그인 여부 체크에 사용 가능)

# 5. 세션 전체 삭제
#   session.clear()
#   모든 세션 데이터를 삭제 (로그아웃 구현시 유용)

# 6. 세션 수정 명시
#   session.modified = True
#   세션 데이터가 변경되었음을 명시적으로 표시, 세션 내용이 변경될 때 자동으로 플라스크가 처리하지 못하는 경우에 유용