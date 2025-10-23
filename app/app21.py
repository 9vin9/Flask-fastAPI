# ## 로깅

# from flask import Flask
# import logging

# app = Flask(__name__)

# # 로그 레벨을 DEBUG로 설정
# # app.logger.setLevel(logging.DEBUG)

# # # 로그를 파일로 저장. 추가적으로 날짜와 시간, 로그 레벨도 포함하도록 함
# # logging.basicConfig(filename='application.log', level=logging.DEBUG,
# #                     format= '%(asctime)s:%(levelname)s:%(message)s')

# @app.route('/')
# def home():
#     # 여기서 각기 다른 로그 레벨의 로그를 생성
#     app.logger.debug('Debug level log')
#     app.logger.info('Info level log')
#     app.logger.warning('Warning level log')
#     app.logger.error('Error level log')
#     app.logger.critical('Critical level log')
#     return 'Hello, World!'

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask
import logging
from logging.handlers import RotatingFileHandler # 👈 파일 핸들러 임포트

app = Flask(__name__)

# ----------------- 로깅 설정 부분 수정 -----------------

# 1. Flask 로거 레벨 설정
app.logger.setLevel(logging.DEBUG)

# 2. 파일 핸들러 생성 및 포맷 설정
file_handler = RotatingFileHandler(
    'application.log', 
    maxBytes=1024 * 1024 * 10, # 파일 최대 크기 10MB 설정
    backupCount=5 # 백업 파일 5개 생성
)

# 포맷 지정
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

# 3. Flask 로거에 핸들러 추가
# 기존의 콘솔 핸들러에 파일 핸들러만 추가하여 로그 파일에 기록합니다.
app.logger.addHandler(file_handler)

# ----------------- 라우트 및 실행 코드 -----------------

@app.route('/')
def home():
    # 여기서 각기 다른 로그 레벨의 로그를 생성
    app.logger.debug('Debug level log')
    app.logger.info('Info level log')
    app.logger.warning('Warning level log')
    app.logger.error('Error level log')
    app.logger.critical('Critical level log')
    return 'Hello, World!'

if __name__ == '__main__':
    # Flask 앱 실행 시 debug=True 환경에서는 로깅 설정이 덮어쓰기 될 수 있으므로, 
    # 로깅 테스트 시에는 잠시 debug=False로 두거나, 
    # 터미널에서 'flask run' 명령을 사용하여 실행할 수 있습니다.
    app.run(debug=True)