from flask import Flask, g, render_template, request
"""
mock user login system.
"""


app = Flask(__name__)

# Mock user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Get user's locale."""
    user_id = request.args.get("login_as")
    if user_id is None:
        return None
    return users.get(int(user_id))


@app.before_request
def before_request():
    """ before request """
    g.user = get_user()


@app.route('/')
def index():
    """ index page  """
    return render_template('5-index.html')
