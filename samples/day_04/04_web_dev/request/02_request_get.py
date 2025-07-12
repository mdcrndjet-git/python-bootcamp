from flask import Flask, render_template, session

app = Flask(__name__)
app.secret_key = "secret"


@app.get("/")
def show_todos():
    if "todos" not in session:
        session["todos"] = []
    return render_template("index.html", todos=session["todos"])


app.run()
