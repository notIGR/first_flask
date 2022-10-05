from flask import Flask
#creates an instance of Flask
app = Flask(__name__)
 
@app.route("/") #app decorator
def index():
    return "<p> Index Page </p>" 
@app.route("/about")
def about():
    return "<p> About Page </p>" 
@app.route("/hello") #app decorator
def hello_world():
    return "<p> Hello, World! </p>"
