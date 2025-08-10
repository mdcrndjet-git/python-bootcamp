from aiohttp.web_routedef import route
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Index Page"

@app.route("/home/")
def home():
    return "Home Page"

@app.route("/profile/")
@app.route("/profiles/")
def profile():
    return "Profile Page"

app.run()
