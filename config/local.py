import os
import sys
import logging
from .settings import Settings, BASE_DIR


class Local(Settings):
    DEBUG = bool(int(os.environ.get('DEBUG', False)))
    ALLOWED_HOSTS = ['*']
    REDIRECT_URI = os.environ.get('REDIRECT_URI', 'https://ed42-183-80-97-64.ap.ngrok.io')
    CSRF_TRUSTED_ORIGINS = [REDIRECT_URI]

    INSTALLED_APPS = Settings.INSTALLED_APPS + ['apps']

    # Swagger settings
    SWAGGER_SETTINGS = {
        'LOGIN_URL': 'admin:login',
        'LOGOUT_URL': 'admin:logout'
    }

    # database settings
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(f"{BASE_DIR}", 'db.sqlite3'),
        }
    }

    # celery settings
    CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379/0')
    CELERY_BACKEND_URL = os.environ.get('CELERY_BACKEND_URL', 'redis://localhost:6379/0')
    CELERY_RESULT_BACKEND = 'django-db'
    CELERY_ACCEPT_CONTENT = ['application/json']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_TIMEZONE = Settings.TIME_ZONE
    CELERY_RESULT_EXTENDED = True

    # proxy settings
    PROXY_URL = os.environ.get('PROXY_URL', 'http://localhost:8000')

    # turn off logging and set celery when test
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        logging.disable(logging.CRITICAL)
        CELERY_TASK_ALWAYS_EAGER = True
        CELERY_TASK_EAGER_PROPAGATES = True
        CELERY_BROKER_URL = 'memory://'
        BROKER_BACKEND = 'memory://'

    if int(os.environ.get('IS_SERVER_DB', False)):
        DATABASES['default'] = {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('DATABASE_NAME', 'bean'),
            'USER': os.environ.get('DATABASE_USER', 'root'),
            'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'root123'),
            'HOST': os.environ.get('DATABASE_HOST', 'db.bean.orb.local'),
            'PORT': os.environ.get('DATABASE_PORT', '5432'),
        }
        DATABASE_POOL_CLASS = 'sqlalchemy.pool.QueuePool'
        DATABASE_POOL_ARGS = {
            'max_overflow': 15,
            'pool_size': 15,
            'recycle': 300,
        }
