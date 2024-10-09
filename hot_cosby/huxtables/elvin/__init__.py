"""
https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html

Scheduler for celery beat asynchronous/periodic tasks
"""

from hot_cosby.src.worker.celery_app import app
from .. import Huxtable


class Elvin(Huxtable):
    @app.on_after_configure.connect
    async def set_schedule(self, sender, **kwargs):
        """ Method which sets the celery beat schedule for repeat async tasks """

        # TODO: Set up periodic tasks once the task functions are available
        sender.add_periodic_task()


__all__ = ['Elvin']
