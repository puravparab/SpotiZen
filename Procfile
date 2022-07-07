# Heroku Specific File
release: python SpotiZen/manage.py migrate
web: gunicorn --pythonpath SpotiZen/SpotiZen SpotiZen.wsgi --preload --log-file -