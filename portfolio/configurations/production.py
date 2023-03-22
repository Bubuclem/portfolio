'''
Configuration for the production environment.
'''
import os
import environ
from portfolio.settings import Base

class Production(Base):
    '''
    The production environment settings.
    '''
    env = environ.Env()
    # Take environment variables from .env file
    environ.Env.read_env(os.path.join(Base.BASE_DIR, '.env'))

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = env('SECRET_KEY')

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = False

    ALLOWED_HOSTS = ['*']
    INTERNAL_IPS = ALLOWED_HOSTS
    # Django reCAPTCHA
    # https://github.com/torchbox/django-recaptcha

    RECAPTCHA_PUBLIC_KEY = env('RECAPTCHA_PUBLIC_KEY')
    RECAPTCHA_PRIVATE_KEY = env('RECAPTCHA_PRIVATE_KEY')
    RECAPTCHA_REQUIRED_SCORE = 0.85

    # Protection contre le « Cross site request forgery »
    # https://docs.djangoproject.com/fr/4.0/ref/csrf/
    # &
    # Intergiciels (« middleware »)
    # https://docs.djangoproject.com/fr/4.0/ref/middleware/

    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 300000
    SECURE_HSTS_PRELOAD = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
