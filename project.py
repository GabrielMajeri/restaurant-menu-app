from flask import Flask

from database import DBSession, Restaurant, MenuItem

app = Flask(__name__)


session = DBSession()


@app.route('/restaurant/<int:restaurant_id>/')
def view_menu_items(restaurant_id):
    output = ''
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id)
    for i in items:
        output += f'{i.name} <br/>'
        output += f'{i.price or ""} <br/>'
        output += f'{i.description or ""} <br/>'
    output += '<br/>'
    return output


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
    app.run()
