# Heroku Specific File
release: python SpotiZen/manage.py migrate
web: gunicorn --pythonpath Spotizen SpotiZen.wsgi --preload --log-file -