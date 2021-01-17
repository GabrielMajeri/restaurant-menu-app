from flask import Flask

from database import DBSession, Restaurant, MenuItem

app = Flask(__name__)


session = DBSession()


@app.route('/')
@app.route('/hello')
def hello_world():
    output = ''
    restaurants = session.query(Restaurant)
    for restaurant in restaurants:
        output += f'<h2>{restaurant.name}</h2>'
        items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
        for i in items:
            output += f'{i.name} <br/>'
            output += f'{i.price or ""} <br/>'
            output += f'{i.description or ""} <br/>'
        output += '<br/>'
    return output


if __name__ == '__main__':
    app.run()
