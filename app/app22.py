## 데이터베이스 CRUD

from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://ijeongbin:mmmm@localhost/db_name'
# SQLAlchemy 인스턴스 초기화
db = SQLAlchemy(app)

#데이터베이스 모델 정의
class User(db.Model):
    # 각필드 정의
    id = db.Column(db.Integer, primary_key=True)    # PK: 사용자 ID
    username = db.Column(db.String(80), unique=True, nullable=False) # 사용자 이름, 중복 불가능 및 필수
    email = db.Column(db.String(120), unique=True, nullable=False) # 이메일 주소, 중복 불가능 및 필수
    
    def __repr__(self):
        return f'<User {self.username}>' # 객체를 문자열로 표현할 때 사용할 형식
    
# 앱 컨텍스트 안에서 DB테이블 생성
with app.app_context():
    db.create_all()
    
@app.route('/')
def index():
    # 데이터 생성(Create)
    new_user = User(username = 'john', email='john@example.com')
    db.session.add(new_user)
    db.session.commit()
    
    # 데이터 조회(Read)
    user = User.query.filter_by(username='john').first()
    
    # 데이터 업데이트 (update)
    user.email = 'john@newexample.com'
    db.session.commit()
    
    # 데이터 삭제(Delete)
    db.session.delete(user)
    db.session.commit()
    
    return 'CRUD operataions completed'