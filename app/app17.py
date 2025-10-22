from flask import Blueprint, Flask

# 첫번째 인자는 블루프린트의 이름
# 두번째 인자는 블루프린트가 정의된 모듈이나 패키지의 이름 (일반적으로 __name__ 변수 사용)

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/login')
def login():
    return '로그인 페이지입니다.'

@auth_blueprint.route('/logout')
def logout():
    return '로그아웃 되었습니다.'

app = Flask(__name__)

# 블루프린트 등록
# url_prefix는 해당 블루프린트의 모든 라우트 앞에 붙게 되는 접두사
app.register_blueprint(auth_blueprint, url_prefix='/auth')