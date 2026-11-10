# Wokku has no separate release step: migrate + collectstatic run as the
# container starts, then gunicorn takes over. bash -lc because Wokku runs
# this line without a shell, and the login shell puts the venv on PATH.
web: bash -lc 'python manage.py migrate --noinput && python manage.py collectstatic --noinput && exec gunicorn app.wsgi --bind 0.0.0.0:$PORT --log-file -'
