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
    session.add(Restaurant(name="Best Diner"))
    session.add(Restaurant(name="Faster Food"))

    i1 = MenuItem(name="Cheeze Pizza", restaurant=r1)
    session.add(i1)

    session.commit()
