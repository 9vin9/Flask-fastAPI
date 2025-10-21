from flask import Flask, render_template

app = Flask(__name__)

@app.route('/messages')
def show_messages():
    return render_template('messages.html')

# test: 1. terminal -> flask run
#       2. open browser -> http://127.0.0.1:5000/messages

# 코드의 중복을 줄이고 유지보수성을 향상시키는 효과적인 방법
# 웹페이지에서 반복해서 사용되는 HTML 구조나 컴포넌트를 매크로로 정의하면
# 필요할 때마다 해당 매크로를 호출하여 재사용할 수 있습니다.
