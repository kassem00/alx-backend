#!/usr/bin/env python3
"""  setup a basic Flask app """


from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


@app.request("/")
def index():
    return render_template("templates/0-index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
