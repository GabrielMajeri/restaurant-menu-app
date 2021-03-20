from flask import Flask, render_template, g, request, redirect, url_for, flash
from flask_minify import minify
from database import DBSession, Restaurant
from sqlalchemy.orm.session import Session
from werkzeug.local import LocalProxy

app = Flask(__name__)
app.secret_key = b'1234'

minify(app=app, html=True, js=True, cssless=True)


def get_db() -> Session:
    if 'db' not in g:
        g.db = DBSession()

    return g.db


@app.teardown_appcontext
def teardown_db(_):
    db: Session = g.pop('db', None)

    if db is not None:
        db.close()


db: Session = LocalProxy(get_db)


@app.route('/')
@app.route('/restaurants')
def view_restaurants():
    restaurants = db.query(Restaurant)
    return render_template('restaurants/index.html', restaurants=restaurants)


@app.route('/restaurants/new', methods=['GET', 'POST'])
def new_restaurant():
    if request.method == 'GET':
        return render_template('restaurants/new.html')
    elif request.method == 'POST':
        name = request.form['name']

        if len(name) < 3:
            flash("Restaurant's name is too short")
            return render_template('restaurants/new.html')

        restaurant = Restaurant(name=name)
        db.add(restaurant)
        db.commit()
        return redirect(url_for('view_restaurants'))


@app.route('/restaurants/<int:restaurant_id>/edit', methods=['GET', 'POST'])
def edit_restaurant(restaurant_id):
    restaurant = db.query(Restaurant).get(restaurant_id)

    if request.method == 'GET':
        return render_template('restaurants/edit.html', restaurant=restaurant)
    elif request.method == 'POST':
        name = request.form['name']

        if len(name) < 3:
            flash("Restaurant's name is too short")
            return render_template('restaurants/edit.html', restaurant=restaurant)

        restaurant.name = name

        db.commit()

        return redirect(url_for('view_restaurants'))


@app.route('/restaurants/<int:restaurant_id>/delete', methods=['GET', 'POST'])
def delete_restaurant(restaurant_id):
    restaurant = db.query(Restaurant).get(restaurant_id)

    if request.method == 'GET':
        return render_template('restaurants/delete.html', restaurant=restaurant)
    elif request.method == 'POST':
        db.delete(restaurant)
        db.commit()

        return redirect(url_for('view_restaurants'))
