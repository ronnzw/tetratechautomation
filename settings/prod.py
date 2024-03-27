from .base import *

import os
from dotenv import load_dotenv


load_dotenv()

SECRET_KEY = os.environ.get('PROD_SECRET_KEY')
DEBUG = os.environ.get('PROD_DEBUG') == "True"
ALLOWED_HOSTS = ['127.0.0.1','www.tetratechautomation.co.zw','tetratechautomation.co.zw','https://tetratechautomation.co.zw','http://tetratechautomation.co.zw']

#Prod
EMAIL_BACKEND = os.environ.get('PROD_EMAIL_BACKEND')
EMAIL_HOST = os.environ.get('PROD_EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('PROD_EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('PROD_EMAIL_HOST_PASSWORD')
EMAIL_PORT = int(os.environ.get('PROD_EMAIL_PORT'))
EMAIL_USE_TLS = os.environ.get('PROD_EMAIL_USE_TLS') == "True"