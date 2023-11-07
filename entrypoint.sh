#!/bin/sh

set -e
echo "Migrating the database before starting the server"
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

echo "runserver"
gunicorn wsgi:application --worker-class=gevent --worker-connections=2000 --workers=8 --keep-alive=8 --bind 0.0.0.0:8000 --log-level=debug
