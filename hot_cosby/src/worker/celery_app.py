from celery import Celery
from ..config import celery as celery_config


def get_app(*args, **kwargs):
    celery = Celery(*args, **kwargs)
    celery.config_from_object(celery_config)
    return celery


app = get_app()
