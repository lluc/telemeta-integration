#!/bin/bash

# paths
app='/srv/app'
static='/srv/static/'
media='/srv/media/'
src='/srv/src/'
log='/var/log/uwsgi/app.log'

# uwsgi params
port=8000
processes=8
threads=8
autoreload=3
uid='www-data'
gid='www-data'

#pip install -U django==1.8.18 django-registration-redux
#pip uninstall -y south
#pip install -e git+https://github.com/Parisson/django-jqchat.git@dj1.8#egg=django-jqchat
#pip install django-debug-toolbar==1.6
#pip install -e git+https://github.com/Parisson/saved_searches.git@dj1.8#egg=saved_searches-2.0.0-beta

export PYTHONPATH=$PWD/telemeta_mshs/apps:$PYTHONPATH

python ./manage.py syncdb
python ./manage.py migrate --noinput -v 3
python ./manage.py bower_install -- --allow-root

# telemeta setup
python ./manage.py telemeta-create-admin-user
python ./manage.py telemeta-create-boilerplate
python ./manage.py telemeta-setup-enumerations

# Delete Timeside database if it exists
cat ./telemeta_mshs/apps/Telemeta/scripts/sql/drop_timeside.sql | python ./manage.py dbshell

if [ $REINDEX = "True" ]; then
    python ./manage.py rebuild_index --noinput
fi

# choose dev or prod mode
if [ "$1" = "--runserver" ]; then
    python ./manage.py runserver 0.0.0.0:8000
else
    python ./manage.py collectstatic --noinput

    # fix media access rights
    find $media -maxdepth 1 -path ${media}import -prune -o -type d -not -user www-data -exec chown www-data:www-data {} \;

    # Start Gunicorn processes
    echo Starting Gunicorn.
    exec gunicorn telemeta_mshs.wsgi:application \
            --bind :$port \
            --workers 3
fi
