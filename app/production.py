from .settings import *
from dotenv import load_dotenv

env_path = os.path.join(BASE_DIR, 'app/.env')
load_dotenv(dotenv_path=env_path)

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['https://filestorage-evotask.herokuapp.com']
