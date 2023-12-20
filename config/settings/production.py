from .base import *

CONFIG = environment_config("production")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

SECRET_KEY = CONFIG.get("SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS = []