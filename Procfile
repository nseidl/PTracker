web: gunicorn app:app --workers 2 --threads 2 -k sync --timeout=300
migrate: python manage.py db upgrade
