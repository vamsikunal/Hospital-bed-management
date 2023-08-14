#!/bin/bash
# Run Django database migrations

python3 manage.py makemigrations
python3 manage.py migrate --noinput

gunicorn hbms.wsgi:application --bind 0.0.0.0:8000 &

unlink /etc/nginx/sites-enabled/default

nginx -g "daemon off;"

# # Start the Django development server
# python3 manage.py runserver 0.0.0.0:8000

# curl localhost:8000
# ``` 