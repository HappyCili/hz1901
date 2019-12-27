import os

from celery import Celery, platforms

from workon import config
# 加载 Django 的 settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "swiper.settings")

celery_app = Celery("worker")
celery_app.config_from_object(config)
celery_app.autodiscover_tasks()
platforms.C_FORCE_ROOT = True