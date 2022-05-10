"""
WSGI config for backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

from gc import collect
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

application = get_wsgi_application()

app = application

# import subprocess
# from dotenv import load_dotenv

# load_dotenv()

# DJANGO_SUPERUSER_USERNAME = str(os.environ.get("DJANGO_SUPERUSER_USERNAME"))
# DJANGO_SUPERUSER_PASSWORD = str(os.environ.get("DJANGO_SUPERUSER_PASSWORD"))
# DJANGO_SUPERUSER_EMAIL = str(os.environ.get("DJANGO_SUPERUSER_EMAIL"))

# migrate_command = [
#     "python3.9",
#     "manage.py",
#     "migrate",
#     "--noinput",
# ]

# makemigration_command = [
#     "python3.9",
#     "manage.py",
#     "makemigrations",
#     "--noinput",
# ]

# create_superuser_command = [
#     "python3.9",
#     "manage.py",
#     "createsuperuser",
#     "--email",
#     f"{DJANGO_SUPERUSER_EMAIL}",
#     "--username",
#     f"{DJANGO_SUPERUSER_USERNAME}",
#     "--noinput",
# ]

# collect_static_command = [
#     "python3.9",
#     "manage.py",
#     "collectstatic",
#     "--noinput",
# ]

# subprocess.run(makemigration_command)
# subprocess.run(migrate_command)
# subprocess.run(create_superuser_command)
# subprocess.run(collect_static_command)