import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #app.config['secret_key'] = secret_key

