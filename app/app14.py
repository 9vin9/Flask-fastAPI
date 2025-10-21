from flask import Flask, render_template

app = Flask(__name__)

@app.route('/zc')
def about_page():
    return render_template('about.html')