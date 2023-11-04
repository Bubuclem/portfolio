'''
Configuration for Development
'''
from portfolio.settings import Base

class Development(Base):
    '''
    Configuration for Development
    '''
    DEBUG = True

    ALLOWED_HOSTS = ['localhost', '127.0.0.1']

    SECRET_KEY='topsecretvalue'
    RECAPTCHA_PRIVATE_KEY='topsecretvalue'
    RECAPTCHA_PUBLIC_KEY='topsecretvalue'