from . import bp
from flask import render_template


@bp.route('/')
@bp.route('/index')
def index():
    context = {
        'user': {'username': 'yurii'},
        'title': 'Social Network'
    }
    return render_template('index.html', **context)


@bp.route('/about')
def about():
    return render_template('about.html')