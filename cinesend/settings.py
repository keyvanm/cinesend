"""
Django settings for cinesend project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
if 'DJANGO_DEBUG' in os.environ:
    DEBUG = (os.environ['DJANGO_DEBUG'] == "True")

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'portal.cinesend.com', 'dev.cinesend.com', 'demo.bitcine.com']

# Application definition
INSTALLED_APPS = (  # The Django sites framework is required
                    'collectfast',
                    'django.contrib.sites',  #
                    'django.contrib.admin',
                    'django.contrib.auth',
                    'django.contrib.contenttypes',
                    'django.contrib.sessions',
                    'django.contrib.messages',
                    'django.contrib.staticfiles',
                    'django.contrib.flatpages',
                    #
                    'storages',
                    's3_folder_storage',
                    # 'easy_thumbnails',
                    'django_extensions',
                    'django_markdown',
                    'markdown_deux',
                    #
                    'allauth',
                    'allauth.account',
                    'allauth.socialaccount',
                    #
                    'bootstrap3',
                    'bootstrapform',
                    'django_tables2',
                    'django_bootstrap_breadcrumbs',
                    'bootstrap3_datetime',
                    'django_select2',
                    'sizefield',
                    #
                    'asset_portal',
                    'user_manager',
                    'vault',
)

SITE_ID = 2

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'cinesend.urls'

WSGI_APPLICATION = 'cinesend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
if 'RDS_DB_NAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Toronto'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'indie_static'),
)
TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'),)
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

TEMPLATE_CONTEXT_PROCESSORS += (  # Required by allauth template tags
                                  "asset_portal.context_processors.debug",
                                  "django.core.context_processors.request",
                                  "django.contrib.auth.context_processors.auth",  # allauth specific context processors
                                  "allauth.account.context_processors.account",
                                  "allauth.socialaccount.context_processors.socialaccount",
)

AUTHENTICATION_BACKENDS = (  # Needed to login by username in Django admin, regardless of `allauth`
                             "django.contrib.auth.backends.ModelBackend",
                             # `allauth` specific authentication methods, such as login by e-mail
                             "allauth.account.auth_backends.AuthenticationBackend",
)

LOGIN_REDIRECT_URL = '/'
# Django all auth settings
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_DISPLAY = lambda user: user.get_full_name()
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_EMAIL_SUBJECT_PREFIX = "CineSend Portal - "
ACCOUNT_SIGNUP_FORM_CLASS = "cinesend.forms.MySignupForm"
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

SELECT2_BOOTSTRAP = True
AUTO_RENDER_SELECT2_STATICS = False
BOOTSTRAP3 = {'javascript_in_head': True, 'include_jquery': True, }

AUTOSLUG_SLUGIFY_FUNCTION = 'django.template.defaultfilters.slugify'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
if 'AWS_STORAGE_BUCKET_NAME' in os.environ:
    DEFAULT_FILE_STORAGE = 's3_folder_storage.s3.DefaultStorage'
    DEFAULT_S3_PATH = "media"
    STATICFILES_STORAGE = 's3_folder_storage.s3.StaticStorage'
    STATIC_S3_PATH = "static"
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_KEY']
    AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']

    MEDIA_ROOT = '/%s/' % DEFAULT_S3_PATH
    MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
    STATIC_ROOT = "/%s/" % STATIC_S3_PATH
    STATIC_URL = '//%s.s3.amazonaws.com/static/' % AWS_STORAGE_BUCKET_NAME
    ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
    AWS_PRELOAD_METADATA = True
else:
    COLLECTFAST_ENABLED = False

# HTTPS Security
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Stripe settings
STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY", "sk_test_4ShobB6XRbglKkS1dOwQd11b")
STRIPE_PUBLIC_KEY = os.environ.get("STRIPE_PUBLIC_KEY", "pk_test_gXaQ6qFcGgqjwEHA1wjYKxcn")
if DEBUG:
    STRIPE_SECRET_KEY = "sk_test_4ShobB6XRbglKkS1dOwQd11b"
    STRIPE_PUBLIC_KEY = "pk_test_gXaQ6qFcGgqjwEHA1wjYKxcn"

MARKDOWN_EDITOR_SKIN = 'simple'

MARKDOWN_DEUX_STYLES = {
    "default": {
        "extras": {
            "code-friendly": None,
        },
        "safe_mode": "escape",
    },
    "trusted": {
        "extras": {
            "code-friendly": None,
        },
        # Allow raw HTML (WARNING: don't use this for user-generated Markdown for your site!).
        "safe_mode": False,
    }
}

# Email
if 'EMAIL_HOST_USER' in os.environ:
    EMAIL_USE_TLS = True
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

# Secret key for prod server
SECRET_KEY = os.environ.get('SECRET_KEY')

# local settings
try:
    from local_settings import *
except ImportError, e:
    pass

try:
    assert SECRET_KEY
except (NameError, AssertionError):
    from secret_key_gen import SECRET_KEY
