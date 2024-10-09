from hot_cosby.src.worker import tasks
from .. import Huxtable


class Theo(Huxtable):
    """ Generic Celery worker interface to our asynchronous tasks """


__all__ = ['Theo']
