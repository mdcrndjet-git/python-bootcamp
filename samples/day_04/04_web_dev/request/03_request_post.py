from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = "secret"


@app.get("/")
def show_todos():
    if "todos" not in session:
        session["todos"] = []
    return render_template("index.html", todos=session["todos"])


@app.post("/")
def add_todo():
    if request.form["todo"]:
        session["todos"].append(request.form["todo"])
        session.modified = True
    return redirect("/")


app.run()
