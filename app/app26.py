## RESTful API

from flask import Flask, request

app = Flask(__name__)

@app.route('/user', methods=['GET', 'POST'])
def manager_user():
    if request.method == 'GET':
        # GET 요청 처리 로직
        return "User data"
    elif request.method == 'POST':
        # POST 요청 처리 로직
        return "Create user"
    elif request.method == 'PUT':
        return "Update user"
    elif request.method == 'DELETE':
        # DELETE 요청 처리 로직
        return "Delete user"
    
# GET 요청: 함수는 "User data"라는 문자열 반환. 실제로는 DB에서 사용자 정보를 가져와 반환하는 로직 들어갈 수 있음
# POST 요청: "Create User"라는 문자열 반환. 실제 상황에서는 DB에 새로운 사용자를 생성하는 로직이 필요
# PUT 요청: "Update user"라는 문자열 반환 실제로는 데이터베이스의 특정 사용자데이터를 수정하는 로직이 들어감. 일반적으로 클라이언트가 서버에 어떤 데이터를 수정하고 싶다고 요청 하면 메서드 사용
# DELETE 요청: "DELETE user"라는 문자열 반환 실제로는 데이터베이스에서 특정 사용자를 삭제하는 로직이 들어감