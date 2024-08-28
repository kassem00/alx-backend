#!/usr/bin/env python3
"""  setup a basic Flask app """


from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """ index home page """
    return render_template("0-index.html")


if __name__ == "__main__":
    """ main funcation """
    app.run(debug=True, host="0.0.0.0")
