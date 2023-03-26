from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    context = {
        'user': {'username': 'yurii'},
        'title': 'Social Network'
    }
    return render_template('index.html', **context)