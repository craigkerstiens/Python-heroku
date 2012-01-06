import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

SECRET_KEY = 'testkey'
DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'dev.db')
DATABASE_CONNECT_OPTIONS = {}
MAIL_SERVER = 'smtp.sendgrid.net'
MAIL_PORT = 587
MAIL_USERNAME = os.environ.get('SENDGRID_USERNAME')
MAIL_PASSWORD = os.environ.get('SENDGRID_PASSWORD')
MAIL_USE_TLS = True
DEFAULT_MAIL_SENDER = 'python@heroku.com'
MAIL_FAIL_SILENTLY = False


del os