#!/bin/bash
# Run Django database migrations

python3 manage.py makemigrations
python3 manage.py collectstatic --noinput
python3 manage.py migrate --noinput

exec gunicorn hbms.wsgi:application --bind 0.0.0.0:8000 

unlink /etc/nginx/sites-enabled/default

nginx -g "daemon off;"