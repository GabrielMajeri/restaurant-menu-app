from flask import Flask, render_template, request, redirect, url_for, flash

from database import DBSession, Restaurant, MenuItem

app = Flask(__name__)
app.secret_key = 'super_secret_key'


@app.route('/restaurant/<int:restaurant_id>/')
def view_menu_items(restaurant_id):
    session = DBSession()
    restaurant = session.query(Restaurant).get(restaurant_id)
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id)
    return render_template('menu.html', restaurant=restaurant, items=items)


@app.route('/restaurant/<int:restaurant_id>/new/', methods=['GET', 'POST'])
def add_menu_item(restaurant_id):
    if request.method == 'POST':
        session = DBSession()
        menu_item = MenuItem(
            name=request.form['name'],
            restaurant_id=restaurant_id
        )
        session.add(menu_item)
        session.commit()
        flash('New menu item created!')

        return redirect(url_for('view_menu_items', restaurant_id=restaurant_id))
    else:
        return render_template('new_menu_item.html', restaurant_id=restaurant_id)


@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/edit/', methods=['GET', 'POST'])
def edit_menu_item(restaurant_id, menu_id):
    session = DBSession()
    item = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        item.name = request.form['name']
        session.commit()
        flash('Menu item edited!')

        return redirect(url_for('view_menu_items', restaurant_id=restaurant_id))
    else:
        return render_template(
            'edit_menu_item.html',
            restaurant_id=restaurant_id,
            item=item
        )


@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/delete/', methods=['GET', 'POST'])
def delete_menu_item(restaurant_id, menu_id):
    session = DBSession()
    item = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        session.delete(item)
        session.commit()
        flash('Menu item deleted!')

        return redirect(url_for('view_menu_items', restaurant_id=restaurant_id))
    else:
        return render_template(
            'delete_menu_item.html',
            restaurant_id=restaurant_id,
            item=item
        )


# JSON routes

@app.route('/restaurant/<int:restaurant_id>/json/')
def get_menu_items_json(restaurant_id):
    session = DBSession()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id)
    return {
        'menu_items': [item.serialize() for item in items]
    }


@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/json/')
def get_menu_item_json(restaurant_id, menu_id):
    session = DBSession()
    item = session.query(MenuItem).get(menu_id)
    return {
        'menu_item': item.serialize()
    }


if __name__ == '__main__':
    app.run()
