# Heroku Specific File
release: python server/manage.py migrate
web: gunicorn --pythonpath server.SpotiZen.wsgi --preload --log-file -