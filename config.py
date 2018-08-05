import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hWmZq4t7w!z%C*F-JaNdRgUjXn2r5u8x'
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'bt_cxt.db')
    #SQLALCHEMY_TRACK_MODIFICATIONS = False
    DB_PATH = os.path.join(basedir, 'bf_cxt_sqlite.db')
