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


@app.route("/order_summary")
def order_summary():
    order = {
        "customer": "Juan Dela Cruz",
        "address": "Manila, Metro",
        "choices": ["Tapsilog", "Fried Chicken", "Extra Rice"],
        "special_notes": "Allergic to peanuts"
    }
    return render_template("order_summary.html", order=order)


app.run()
