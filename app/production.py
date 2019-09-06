from .settings import *


DEBUG = bool(int(os.environ['DEBUG_ON']))

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['filestorage-evotask.herokuapp.com']


AWS_S3_SECURE_URLS = False       # use http instead of https
AWS_QUERYSTRING_AUTH = False                # don't add complex authentication-related query parameters for requests
AWS_S3_ACCESS_KEY_ID = os.environ['AWS_S3_ACCESS_KEY_ID']                # Your S3 Access Key
AWS_S3_SECRET_ACCESS_KEY = os.environ["AWS_S3_SECRET_ACCESS_KEY"]
AWS_STORAGE_BUCKET_NAME = os.environ["AWS_STORAGE_BUCKET_NAME"]
AWS_S3_HOST = os.environ["AWS_S3_HOST"]  # Change to the media center you chose when creating the bucket

DEFAULT_FILE_STORAGE = "app.s3utils.MediaS3BotoStorage"

import ssl
if hasattr(ssl, '_create_unverified_context'):
   ssl._create_default_https_context = ssl._create_unverified_context