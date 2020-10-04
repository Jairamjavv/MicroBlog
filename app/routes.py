from flask import render_template
from app import app


@app.route("/")
@app.route("/index")
def index():
    user = {'username': 'Jairam'}
    posts = [
        {
            'author': 'Je Mess Cameraman',
            'title': 'How to make Ice Water'
        },
        {
            'author': 'Jairam',
            'title': 'How to make Hot water'
        },
        {
            'author': 'Jairam',
            'title': 'How to make Ice cubes - Freezer Version'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
