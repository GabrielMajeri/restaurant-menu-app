from flask import Flask, render_template
from flask_minify import minify

app = Flask(__name__)
minify(app=app, html=True, js=True, cssless=True)


@app.route('/')
@app.route('/restaurants')
def view_restaurants():
    return render_template('restaurants.html')


@app.route('/restaurants/new')
def new_restaurant():
    return 'New restaurant page'


# TODO: https://flask.palletsprojects.com/en/1.1.x/tutorial/database/
