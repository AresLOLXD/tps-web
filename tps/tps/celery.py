from celery import Celery
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tps.settings")

from tasks.serializers import DjangoPKSerializer

DjangoPKSerializer.register()

app = Celery("tps")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
