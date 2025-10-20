from flask import Flask, request



app = Flask(__name__)

@app.route('/query')
def query_params():
    language = request.args.get('language')
    return f"Requested language: {language}"