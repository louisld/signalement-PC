import os

from signalement.utils import make_dir

class BaseConfig(object):

    PROJECT = "signalement"

    PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    DEBUG = False
    TESTING = True

    ADMINS = ['email@example.com]

    SECRET_KEY = "rejhbviuzreghéç_hoYGF7FGI8hzf"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    LANGUAGES = {
        'fr': 'Français',
        'en': 'English'
    }

class DefaultConfig(BaseConfig):

    DEBUG = True

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://signalement:carotte@localhost/signalement?charset=utf8'

class TestConfig(BaseConfig):
    TESTING = True
    CSRF_ENABLED = False
