from .settings import *


DEBUG = bool(os.environ['DEBUG_ON'])

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['filestorage-evotask.herokuapp.com']
