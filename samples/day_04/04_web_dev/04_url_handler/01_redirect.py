from flask import Flask, redirect

app = Flask(__name__)


@app.route("/user/<username>")
def profile(username):
    if username != "admin":
        return redirect('/login')
    return "Welcome Admin"


@app.route('/login')
def login():
    return "Please login"


app.run()
