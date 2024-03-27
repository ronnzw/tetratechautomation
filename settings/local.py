from .base import *

import os
from dotenv import load_dotenv


load_dotenv()

SECRET_KEY = os.environ.get('LOCAL_SECRET_KEY')
DEBUG = os.environ.get('LOCAL_DEBUG') == 'True'
ALLOWED_HOSTS = ['*']

# Email settings
EMAIL_BACKEND = os.environ.get('LOCAL_EMAIL_BACKEND')
ACCOUNT_EMAIL_VERIFICATION = os.environ.get('LOCAL_ACCOUNT_EMAIL_VERIFICATION')