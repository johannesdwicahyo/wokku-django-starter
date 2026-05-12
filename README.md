# wokku-django-starter

Bare-bones Django 5 app on SQLite, configured to one-click-deploy on [Wokku](https://wokku.cloud).

## Deploy

[![Deploy to Wokku](https://wokku.cloud/deploy-button.svg)](https://wokku.cloud/templates/django)

Click → pick a tier → live at `https://<your-app>.wokku.cloud` in ~90 seconds.

## Local development

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
# open http://127.0.0.1:8000
```

## What's inside

- Django 5.1 with SQLite default storage.
- `gunicorn` for production WSGI.
- `whitenoise` serves compressed static files (no separate CDN required).
- `psycopg[binary]` pre-installed — swap SQLite for Postgres later by changing `DATABASES` in `app/settings.py` and adding a Postgres addon.
- `release` Procfile command runs `migrate` + `collectstatic` on every deploy.

Runtime: Python 3.12.7 (pinned in `runtime.txt`).

After deploy, set `SECRET_KEY` and `DEBUG=False` via the Wokku dashboard:

```
wokku config:set SECRET_KEY=$(openssl rand -hex 64) DEBUG=False
```
