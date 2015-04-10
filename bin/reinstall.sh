#!/bin/bash

sudo -u postgres dropdb pyclub
sudo -u postgres createdb pyclub

python manage.py makemigrations
python manage.py migrate

python manage.py loaddata initial_user --traceback
