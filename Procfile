# Heroku Specific File
release: python server/manage.py migrate
web: gunicorn server.SpotiZen.wsgi --preload --log-file -