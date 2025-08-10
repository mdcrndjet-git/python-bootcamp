from aiohttp.web_routedef import route
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<b><u>Intro Boys</u></b> Page"

@app.route("/hobby/")
@app.route("/hobbies/")
def home():
    return "<b><u>Kill time</u></b> Page"

@app.route("/opinion/<topic>")
@app.route("/opinions/<topic>")
def profile_dynamic(topic):
    return f"<b><u>{topic}</u></b> Page"

@app.route("/opinion/food")
def food():
    return "<b><u>Pangbara at Panulak</u></b> Page"

app.run()
