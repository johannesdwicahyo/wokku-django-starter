# Wokku has no separate release step: migrate + collectstatic run as the
# container starts, then gunicorn takes over.
web: python manage.py migrate --noinput && python manage.py collectstatic --noinput && exec gunicorn app.wsgi --bind 0.0.0.0:$PORT --log-file -
