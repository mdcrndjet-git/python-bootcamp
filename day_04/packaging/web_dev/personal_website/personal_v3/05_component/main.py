from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    now = datetime.now()
    return render_template('introduction_v2.html', hour=now.hour)


@app.route("/hobby/")
@app.route("/hobbies/")
def hobby():
    """
    hobbies = ['Play Stardew', 'Write Essay', 'Casual Walk']
    return render_template('hobbies.html', hobbies=hobbies)
    """
    hobbies = ['Chess', 'Scrabble', 'Walk']
    return render_template('hobbies_v2.html', hobbies=hobbies)

@app.route("/opinion/food")
def food():
    """
    foods = ['Fried Chicken', 'Fries', 'Ice Cream']
    return render_template('food.html', foods=foods)
    """

    foods = {
        "pambara":["Morning Pandesal","Laing","Oats and Salad"],
        "panulak":["Water","Fresh Buko Juice"]
    }
    return render_template('food_v2.html', foods=foods)


@app.route("/opinion/<topic>")
@app.route("/opinions/<topic>")
def opinion(topic):
    return render_template('opinion_v2.html', topic=topic)


@app.route("/skills")
def skills():
    """
    skill_levels = {
        "Painting": "Intermediate",
        "Dancing": "Abysmal",
        "Singing": "Poor",
        "Translation": "Proficient",
        "Eating": "Professional"
    }
    return render_template("skills.html", skills=skill_levels)
    """
    skill_levels = {
        "Drawing": "Intermediate",
        "Trading": "Beginner",
        "Eating": "Expert"
    }
    return render_template("skills_v2.html", skills=skill_levels)


app.run()
