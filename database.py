from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from tables import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurant-menu.db', echo=False)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

if __name__ == '__main__':
    Base.metadata.drop_all()
    Base.metadata.create_all(engine)

    session = DBSession()

    r1 = Restaurant(name="Tony's Pizzeria")
    session.add(r1)
    r2 = Restaurant(name="Best Diner")
    session.add(r2)
    r3 = Restaurant(name="Faster Food")
    session.add(r3)

    item = MenuItem(name="Cheeze Pizza", restaurant=r1)
    session.add(item)
    item = MenuItem(name="Diabolica", restaurant=r1)
    session.add(item)

    item = MenuItem(name="Fried Fish", restaurant=r2)
    session.add(item)

    item = MenuItem(name="Hamburger", price="$5", restaurant=r3)
    session.add(item)

    session.commit()
