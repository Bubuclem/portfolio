from portfolio.settings import Base

class Github(Base):
    DEBUG = True

    ALLOWED_HOSTS = ['localhost', 'github.dev']
    INTERNAL_IPS = ALLOWED_HOSTS

    SECRET_KEY='topsecretvalue'
    RECAPTCHA_PRIVATE_KEY='topsecretvalue'
    RECAPTCHA_PUBLIC_KEY='topsecretvalue'

    # Protection contre le « Cross site request forgery »
    # https://docs.djangoproject.com/fr/4.0/ref/csrf/
    # &
    # Intergiciels (« middleware »)
    # https://docs.djangoproject.com/fr/4.0/ref/middleware/

    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = False
    SECURE_HSTS_SECONDS = 300000
    SECURE_HSTS_PRELOAD = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True