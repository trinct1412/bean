from __future__ import absolute_import
import os
import configurations

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.local')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Local')

configurations.setup()

app = Celery('sf', enable_utc=False)
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    # sender.add_periodic_task(300.0, outlook_sync_local.s(), name='outlook_sync_local')
    ...


if __name__ == '__main__':
    app.start()
