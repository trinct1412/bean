import os
from configurations import Configuration
from config.utils import InstalledAppsMixin

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def generate_folder_needed(_dir):
    if not os.path.exists(_dir):
        os.makedirs(_dir)


generate_folder_needed(BASE_DIR + '/public/staticfiles')
generate_folder_needed(BASE_DIR + '/public/media')
generate_folder_needed(BASE_DIR + '/public/static')
generate_folder_needed(BASE_DIR + '/public/logging')


class Settings(InstalledAppsMixin, Configuration):
    SECRET_KEY = '(ves6bcd7s2ayw!-5ov&b5+c)nm9-x741-zsj_7g#5l*%*!0hq'
    ALLOWED_HOSTS = ["*", "localhost"]
    INSTALLED_APPS_DISCOVER = True

    ROOT_URLCONF = 'urls'
    WSGI_APPLICATION = 'wsgi.application'

    # Setting auto fields
    DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

    # Timezone settings
    LANGUAGE_CODE = 'en-us'
    TIME_ZONE = 'UTC'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True

    # Apps default
    DEFAULT_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]

    THIRD_PARTY_APPS = [
        'rest_framework',
        'rest_framework_swagger',
        'django_filters',
        'drf_yasg',
        'django_celery_results',
        'django_celery_beat',
        'rest_framework_simplejwt',
        'corsheaders',
    ]

    INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS

    MIDDLEWARE = [
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware'
    ]

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                    'django.template.context_processors.media',
                ],
            },
        },
    ]

    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ]

    # config media and static
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, "public/media")
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'public/static')
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'public/staticfiles'),
    )
    # STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )

    # logging
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
                'style': '{',
            },
            'simple': {
                'format': '{levelname} {message}',
                'style': '{',
            },
        },
        'loggers': {
            'django': {
                'handlers': ['file'],
                'level': 'DEBUG',
                'propagate': True,
            },
            'celery': {
                'handlers': ['console'],
                'level': 'DEBUG',
                'propagate': True,
            },
        },
        'handlers': {
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': f'{BASE_DIR}/public/logging/debug.log',
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
            },
        },

    }

    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.TokenAuthentication',
            'rest_framework.authentication.BasicAuthentication',
            'rest_framework.authentication.SessionAuthentication',
            'rest_framework_simplejwt.authentication.JWTAuthentication',
        ),
        'DEFAULT_PERMISSION_CLASSES': (
            'rest_framework.permissions.AllowAny',
            'rest_framework.permissions.IsAuthenticatedOrReadOnly',
        ),
        'TEST_REQUEST_RENDERER_CLASSES': (
            'rest_framework.renderers.MultiPartRenderer',
            'rest_framework.renderers.JSONRenderer',
            'rest_framework.renderers.TemplateHTMLRenderer',
        ),
        'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
        'TEST_REQUEST_DEFAULT_FORMAT': 'json',
        'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
        'EXCEPTION_HANDLER': 'config.exceptions.exceptions_handler',
    }
