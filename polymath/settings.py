import os
import dj_database_url

# Django settings for polymath project.

DEBUG = True if os.environ.get('DJANGO_DEBUG', None) == '1' else False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Geoff Kimball', 'gakimball@bsu.edu'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'polymath',  # Or path to database file if using sqlite3.
        'USER': 'geoff',  # Not used with sqlite3.
        'PASSWORD': '',  # Not used with sqlite3.
        'HOST': 'localhost',  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',  # Set to empty string for default. Not used with sqlite3.
    }
}
if DEBUG is not True:
    DATABASES = { 'default': dj_database_url.config() }
SOUTH_DATABASE_ADAPTERS = { 'default':'south.db.postgresql_psycopg2' }

# Allow all host headers
ALLOWED_HOSTS = ['*']

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# We're localizin' but not internationalizin'
USE_I18N = False
USE_L10N = True
USE_TZ = True

# Media
MEDIA_ROOT = '/Applications/MAMP/htdocs/polymath/static/uploads'
MEDIA_URL = 'http://0.0.0.0:5000/static/uploads/'

# Static
STATIC_ROOT = ''
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    '/Applications/MAMP/htdocs/polymath/static',
)

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

if DEBUG is False:
    DEFAULT_FILE_STORAGE = lambda: S3BotoStorage(location='media')
    STATICFILES_STORAGE  = lambda: S3BotoStorage(location='static')
    MEDIA_ROOT = '/uploads/'
    MEDIA_URL = 'http://polymathic.s3.amazonaws.com/'


# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'Kittens')

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'polymath.urls'

WSGI_APPLICATION = 'polymath.wsgi.application'

TEMPLATE_DIRS = (
    '/Applications/MAMP/htdocs/polymath/templates'
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    # "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    "polymath.context_processors.current_dept",
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    'apps.music',
    'apps.video',
    # 'apps.writing',
    # 'apps.audio',
    # 'apps.blog',

    'apps.people',
    # 'apps.events',
    # 'apps.promos',

    'south',
    'django_extensions',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Static asset configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))