from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('dashboard.html')


@app.route("/orders/<area>")
def orders(area):
    return render_template("orders.html", area=area)


@app.route("/menu")
def menu():
    items = ["Adobo", "Tapsilog", "Spaghetti", "Burger", "Chicken"]
    return render_template("menu.html", items=items)


app.run()
