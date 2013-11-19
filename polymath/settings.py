import os
import os.path
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
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
DATABASES['default'] = dj_database_url.config()
SOUTH_DATABASE_ADAPTERS = { 'default': 'south.db.postgresql_psycopg2' }

# Allow all host headers
ALLOWED_HOSTS = ['*']

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# We're localizin' but not internationalizin'
USE_I18N = False
USE_L10N = True
USE_TZ = True

# Project root
PROJECT_DIR = os.path.dirname(__file__)

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static'),
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'Kittens')

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

# Local media settings
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'static/uploads')
MEDIA_URL = 'http://0.0.0.0:5000/static/uploads/'
STATIC_ROOT = ''
STATIC_URL = '/static/'

# Deployment media settings
if DEBUG is False:
    from storages.backends.s3boto import S3BotoStorage
    DEFAULT_FILE_STORAGE = 'polymath.s3utils.MediaS3Storage'
    STATICFILES_STORAGE  = 'polymath.s3utils.StaticS3Storage'
    MEDIA_ROOT = '/uploads/'
    MEDIA_URL = 'http://polymathic.s3.amazonaws.com/media/'
    STATIC_ROOT = '/static/'
    STATIC_URL = 'http://polymathic.s3.amazonaws.com/static/'

DEBUG = True

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

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
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'polymath.urls'

WSGI_APPLICATION = 'polymath.wsgi.application'

# Templates
TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates')
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
    'apps.writing',
    # 'apps.audio',
    # 'apps.blog',

    'apps.people',
    # 'apps.events',
    # 'apps.promos',

    'south',
    'django_extensions',
    'debug_toolbar',
    # 'colors',
)

# Django Toolbar
if DEBUG is True:
    DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.version.VersionDebugPanel',
        'debug_toolbar.panels.timer.TimerDebugPanel',
        'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
        'debug_toolbar.panels.headers.HeaderDebugPanel',
        'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
        'debug_toolbar.panels.template.TemplateDebugPanel',
        'debug_toolbar.panels.sql.SQLDebugPanel',
        'debug_toolbar.panels.signals.SignalDebugPanel',
        'debug_toolbar.panels.logger.LoggingPanel',
    )
    INTERNAL_IPS = ('127.0.0.1', '0.0.0.0')

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