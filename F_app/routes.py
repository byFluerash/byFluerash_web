
from flask import render_template
from F_app import app


@app.route("/")
def home():
    return "Hello, Fadfsadfasdfasd!"

@app.route('/cat')
def cat():
    user = {'username': 'CAT'}
    return render_template('cat.html', title='Home', user=user)

@app.route('/dog')
def dog():
    user = {'username': 'DOG'}
    return render_template('dog.html', title='Home', user=user)

@app.route('/fox')
def fox():
    user = {'username': 'FOX'}
    return render_template('fox.html', title='Home', user=user)

@app.route('/history')
def history():
    user = {'username': 'History'}
    return render_template('history.html', title='Home', user=user) 

@app.route('/history/static/<uuid>')
def history_static():
    user = {'username': 'History-Static-number'}
    return render_template('history_static_number.html', title='Home', user=user)  