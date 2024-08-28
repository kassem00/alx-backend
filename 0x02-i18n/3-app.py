#!/usr/bin/env python3
from flask import Flask, render_template, request
from flask_babel import Babel, _, gettext


class Config:
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


@app.route("/")
def index():
    return render_template("3-index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
