import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'hard to guess string'
    FLASKY_ADMIN = 'xiaowubike'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MONGODB_SETTINGS = {
        'db': 'xiaowubike',
        'host': '192.168.56.101',
        'username': 'xiaowu',
        'password': '123568',
        'port': 27017
    }


config = {'default': DevelopmentConfig}
