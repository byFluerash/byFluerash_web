
from flask import render_template
from F_app import app


@app.route("/")
def home():
    return "Hello, Fadfsadfasdfasd!"

@app.route('/cat')
def cat():
    user = {'username': 'Miguel'}
    return render_template('cat.html', title='Home', user=user)