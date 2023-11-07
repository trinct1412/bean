from .celery import app as celery_app
from .local import Local as local

__all__ = ('celery_app',)
