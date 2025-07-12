from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template(
        'base.html',
        title='Home',
        heading='Home page',
        subtitle='The landing page goes here',
        content="This page is mainly to showcase what components do"
    )


@app.route('/about/')
def about():
    return render_template(
        'base.html',
        title='About',
        heading='About page',
    )


@app.route('/extra/')
def bonus():
    return render_template(
        'extra.html',
        title='Extra',
        heading='Extra page',
    )


app.run()
