WorkDirectory:


    ├─┬ bean
    │ ├─┬ api                          # Directory for api using rest-api
    │ │ ├─┬ filters                     # Directory for filter
    │ │ ├─┬ serializers                 # Directory for serializers
    │ │ ├─┬ urls                        # Directory for urls
    │ │ ├─┬ views                       # Directory for views
    │ │ ├───┬ url.py                    # Python file general url
    │ ├─┬ apps                         # Directory for manage logs
    │ │ ├─┬ manager                     # Directory for manager
    │ │ ├─┬ migrations                  # Directory for migrations
    │ │ ├─┬ models                      # Directory for models
    │ │ ├─┬ tasks                       # Directory for tasks celery
    │ │ ├───┬ admin.py                  # Python file show model admin view
    │ │ ├───┬ apps.py                   # Python file register application settings
    │ │ ├───┬ view.py                   # Python file views
    │ ├─┬ tests                        # Directory for test
    │ │ ├─┬ unit_test                  # Directory for unit_test
    │ ├─┬ config                       # Directory for all config django
    │ ├─┬ initial_data                 # Directory for initial_data
    │ │ ├─┬ tasks                      # Directory for tasks celery
    │ ├─┬ proxy                        # Directory for proxy
    │ ├─┬ spiders                      # Directory for scrapy
    ├─ docker-compose.yml             # Docker build django
    ├─ Dockerfile                     # Docker build sh
    ├─ entrapoint.sh                  # Docker build sh
    ├─ requirements.txt               # Package file requirements
    ├─ manage.py                      # Python file use command django
    ├─ wsgi.py                        # Python file run django
    ├─ url.py                         # Python file general url


Requiments:

    - python: 3.10.10
    - django: 4.2.6
    - redis : 7.0.4

Run Project:

    1. pip install virtualenv
    2. python -m virtualenv env
    3. source env/bin/activate
    4. pip install -r requirements.txt
    5. brew install redis
    6. brew services start redis
    7. celery -A config.celery worker -B -l info
    8. python manage.py runserver

Run Project By Docker:

    pip freeze > requirements.txt
    docker-compose up


Env Config:

    # Database
    DATABASE_NAME=db_name
    DATABASE_USER=db_user
    DATABASE_PASSWORD=db_password
    DATABASE_HOST=db_host
    DATABASE_PORT=db_port
    
    # Facebook
    FACEBOOK_APP_ID=facebook_app_id
    FACEBOOK_APP_SECRET=facebook_app_secret
    
    # Celery
    CELERY_BROKER_URL=broker_celery
    CELERY_BACKEND_URL=backend_url

    # Proxy
    PROXY_URL=proxy_server

    # System
    DEBUG=0
    IS_SERVER_DB=1
    REDIRECT_URI=current_url_sever
    DJANGO_CONFIGURATION=Local
    DJANGO_SETTINGS_MODULE=config.local