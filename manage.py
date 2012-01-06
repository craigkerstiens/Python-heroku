# manage.py

from flaskext.script import Manager
import requests, os

from demo import app

manager = Manager(app)

if __name__ == "__main__":
    manager.run()