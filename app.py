from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/restaurants')
def view_restaurants():
    return render_template('restaurants.html')


@app.route('/restaurants/new')
def new_restaurant():
    return 'New restaurant page'


# TODO: https://flask.palletsprojects.com/en/1.1.x/tutorial/database/
