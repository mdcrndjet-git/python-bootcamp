from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    #return "Index Page"
    return "Welcome to the starting page"


app.run()
