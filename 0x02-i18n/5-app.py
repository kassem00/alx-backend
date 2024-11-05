#!/usr/bin/env python3
"""Flask app with Babel for i18n and l10n."""


from flask import Flask, render_template, request, g
from flask_babel import Babel, _, gettext, get_locale


class Config:
    """Flask app config."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Get user's locale."""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


app.jinja_env.globals['get_locale'] = get_locale


@app.route("/")
def index() -> str:
    """Render homepage."""
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
