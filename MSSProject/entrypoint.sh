#!/bin/sh
echo "PRESTART BACKEND-SERVER"
echo "APPLAY MIGRATIONS"
python manage.py migrate
echo "CREATE FAKE DATA"
python manage.py create_fake_data
echo "RUN SERVER"
python manage.py runserver 0.0.0.0:5000