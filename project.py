from flask import Flask, render_template

from database import DBSession, Restaurant, MenuItem

app = Flask(__name__)


@app.route('/restaurant/<int:restaurant_id>/')
def view_menu_items(restaurant_id):
    session = DBSession()
    restaurant = session.query(Restaurant).get(restaurant_id)
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id)
    return render_template('menu.html', restaurant=restaurant, items=items)


@app.route('/restaurant/<int:restaurant_id>/new/')
def add_menu_item(restaurant_id):
    return 'Add a new menu item'


@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/edit/')
def edit_menu_item(restaurant_id, menu_id):
    return 'Edit a menu item'


@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/delete/')
def delete_menu_item(restaurant_id, menu_id):
    return 'Delete a menu item'


if __name__ == '__main__':
    # Need to disable multithreading, since SQLite doesn't support it.
    app.run()
