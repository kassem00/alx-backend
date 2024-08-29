#!/usr/bin/env python3
"""This module sets up a Flask application with Babel integration
for internationalization (i18n) and localization (l10n).
"""


from flask import Flask, render_template, request, g
from flask_babel import Babel, _, gettext, get_locale


class Config:
    """
    Config class defines the configuration
    settings for the Flask application,
    including supported languages and default locale/timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Determines the best match for the user's
    preferred language from the supported languages."""
    user = getattr(g, 'user', None)
    if user is not None:
        return user.locale
    return request.accept_languages.best_match(['en', 'fr'])


app.jinja_env.globals['get_locale'] = get_locale


@app.route("/")
def index() -> str:
    """
    Renders the homepage template, applying the appropriate
    translations based on the user's language preference."""
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
