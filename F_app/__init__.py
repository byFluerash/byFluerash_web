# from flask import Flask
# from flask import render_template
# from datetime import datetime
# import re

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Hello, Flask!"

# @app.route("/hello/<name>")
# def hello_there(name = None):
#     return render_template(
#         "cat.html",
#         name=name,
#         date=datetime.now()
#     )

from flask import Flask

app = Flask(__name__)

from F_app import routes