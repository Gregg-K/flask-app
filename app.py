from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "welcome"

@app.route("/about")
def about():
    return "This is my first Flask App"

@app.route("/contact")
def contact():
    return "contact page"