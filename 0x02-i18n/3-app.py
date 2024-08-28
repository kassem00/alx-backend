#!/usr/bin/env python3
"""Setup a Flask app with Babel for i18n and l10n"""


from flask import Flask, render_template, request, g
from flask_babel import Babel, _, gettext, get_locale


class Config:
    """Configuration class for Flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ determine best lang ever created """
    user = getattr(g, 'user', None)
    if user is not None:
        return user.locale
    return request.accept_languages.best_match(['en', 'fr'])


app.jinja_env.globals['get_locale'] = get_locale


@app.route("/")
def index():
    """ index fun """
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
