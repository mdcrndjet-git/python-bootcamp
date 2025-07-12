from flask import Flask, redirect, abort

app = Flask(__name__)


@app.route("/user/<username>")
def profile(username):
    if username != "admin":
        return redirect('/login')
    return "Welcome Admin"


@app.route('/login')
def login():
    abort(501)


@app.errorhandler(501)
def handle_501_error(error):
    return "Undetected visitor"


app.run()
