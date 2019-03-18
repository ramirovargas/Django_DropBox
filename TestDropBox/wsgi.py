"""
WSGI config for TestDropBox project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TestDropBox.settings')



# Subir un archivo

with open("/Users/rvargas/Downloads/technology-radar-vol-19-en.pdf", "rb") as f:
    settings.DBX.files_upload(f.read(), '/test.pdf', mute = True)


# Lista los archivos que tengo

application = get_wsgi_application()
for entry in settings.DBX.files_list_folder('').entries:
    print(entry.name)
