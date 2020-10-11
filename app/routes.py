from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    forms = LoginForm()
    if forms.validate_on_submit():
        flash('Login user {}'.format(forms.username.label))
        return redirect(url_for('index'))
    return render_template('login.html', title='Login Page', forms=forms)
