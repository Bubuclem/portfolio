import environ
import os
from portfolio.settings import Base

class Production(Base):
    env = environ.Env()
    # Take environment variables from .env file
    environ.Env.read_env(os.path.join(Base.BASE_DIR, '.env'))

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = env('SECRET_KEY')

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    ALLOWED_HOSTS = ['*']
    INTERNAL_IPS = ALLOWED_HOSTS
    # Django reCAPTCHA
    # https://github.com/torchbox/django-recaptcha

    RECAPTCHA_PUBLIC_KEY = env('RECAPTCHA_PUBLIC_KEY')
    RECAPTCHA_PRIVATE_KEY = env('RECAPTCHA_PRIVATE_KEY')
    RECAPTCHA_REQUIRED_SCORE = 0.85