
import django_heroku
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'ecommercebd302@gmail.com' 
EMAIL_HOST_PASSWORD = '12345%$#@!'

EMAIL_PORT = 587
EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = '<ecommercebd302@gmail.com>'
MANAGERS = (('admin','ecommercebd302@gmail.com'),)

ADMINS = MANAGERS


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&b$fa5w%pnzfti$m$m@3+w%c3z8-0z1e4on+5&^r5*=x&k!gmf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['agdebebe.herokuapp.com']

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATIC_URL = '/static/'

# LOGIN_REDIRECT_URL = '/'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
ASGI_APPLICATION = 'ecommerce.routing.application'


django_heroku.settings(locals())

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_FILE_STORAGE = 'storages.backends.dropbox.DropBoxStorage'

DROPBOX_OAUTH2_TOKEN = 'XD92lvBM72AAAAAAAAAADEYlDKp-XNYl3XwzLou29lcnEPDOmPrxyubxxS67Z9Dm'

DROPBOX_ROOT_PATH  = 'ecommerce-bucket'



CORS_REPLACE_HTTPS_REFERER      = True
HOST_SCHEME                     = "https://"
SECURE_PROXY_SSL_HEADER         = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT             = True
SESSION_COOKIE_SECURE           = True
CSRF_COOKIE_SECURE              = True
SECURE_HSTS_INCLUDE_SUBDOMAINS  = True
SECURE_HSTS_SECONDS             = 1000000
SECURE_FRAME_DENY               = True