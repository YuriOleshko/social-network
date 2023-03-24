from app.auth import bp


@bp.route('/')
def index():
    return 'hello from auth'