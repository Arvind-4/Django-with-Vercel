"""
WSGI config for backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os, pathlib, dotenv

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR / '.env'

if ENV_FILE.exists():
	dotenv.read_dotenv(str(ENV_FILE))
# dotenv.read_dotenv(str(ENV_FILE))

from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'backend.settings'

app = get_wsgi_application()