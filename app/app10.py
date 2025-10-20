from flask import Flask, make_response

app = Flask(__name__)

@app.route('/response')
def json_example():
    resp = make_response("Hello with header", 200)
    resp.headers['Custom-Header'] = 'CustomValue'
    return resp

# 200 : OK
# 201 Created : 요청 성공적으로 처리되어 새 리소스 생성
# 400 Bad Request : 서버가 요청 이해하지 못함
# 401 Unauthorized: 인증이 필요한  페이지 요청
# 403 Forbidden : 서버가 요청 거부
# 404 Not Found : 요청한 리소스 찾을 수 없음
# 500 Internal Server Error : 서버 내부 에러 발생