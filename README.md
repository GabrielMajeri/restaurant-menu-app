# Restaurant menu app

Simple web app for managing a list of restaurants and their menus.

This repo contains the project I implemented as part of the [Full Stack Foundations](https://www.udacity.com/course/full-stack-foundations--ud088) course from Udacity.

## Tech stack

- [Python 3](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) web framework
- [SQLAlchemy](https://www.sqlalchemy.org/) object-relational mapper
- [SQLite](https://www.sqlite.org/index.html) database

## Dependencies

If you have pip, you can install all of the required dependencies as listed
in the [requirements file](requirements.txt).

## Running

You can start a local Flask development server by running:

```bash
FLASK_ENV=development flask run
```

## Generating the ER diagram

Install [ERAlchemy](https://pypi.org/project/ERAlchemy/) and its dependencies and then run:

```bash
eralchemy -i sqlite:///restaurant-menu.db -o erd.pdf
```
