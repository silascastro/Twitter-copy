import os.path
baseDir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'mysql://root:qwert123@localhost/toiltor'
DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'qwert123'