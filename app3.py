from flask import Flask,request
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "Logging in..."
    else:
        return "Login Form"
    
#test: 1. Send a GET request to /login and verify the response is "Login Form".
#       terminal command: curl -X GET http://127.0.0.1:5000/login
#test: 2. Send a POST request to /login and verify the response is "Logging in...".
