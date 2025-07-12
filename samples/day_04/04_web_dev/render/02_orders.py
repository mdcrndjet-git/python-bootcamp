from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/orders/<area>")
def orders(area):
    return render_template("orders.html", area=area)


app.run()
