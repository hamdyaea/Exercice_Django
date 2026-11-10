# Merchex — Django Learning Project

Developer: Hamdy Abou El Anein
Contact: hamdy.aea@protonmail.com
License: GNU GPL v3 (see LICENSE).

A small educational Django web application modernized to the supported
Django 5.2 LTS series.

## Local development

```sh
cd django-web-app
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
export DJANGO_DEBUG=1
python merchex/manage.py check
python merchex/manage.py test
python merchex/manage.py runserver 127.0.0.1:8000
```

When `DJANGO_DEBUG=1`, a random development-only secret key is generated
at startup unless `DJANGO_SECRET_KEY` is set. Do not use this mode in
production; restarting invalidates signed sessions.

## Production safeguards

Set `DJANGO_SECRET_KEY` to a new, private high-entropy value and
`DJANGO_ALLOWED_HOSTS` to your actual hostnames. Debug is disabled by
default, and secure cookies are enabled when debug is off.

**The historical public source contained a hard-coded Django secret key.**
It has been removed from the current code, but remains in Git history.
If it was ever deployed, rotate it and invalidate affected sessions.
This modernization does not rewrite Git history or deploy the application.

Use a proper WSGI/ASGI server, HTTPS, database backups and Django's
deployment checklist before publishing this app.

The original historical source remains accessible in Git history;
no additional `old` branch was created because it would preserve the
exposed key as an easy-to-find reference.
