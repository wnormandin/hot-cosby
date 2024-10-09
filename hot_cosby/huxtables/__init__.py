import abc
import datetime
from pydantic import BaseModel
from hot_cosby.src import mongo
from hot_cosby.src.config.globals import MongoCollections
from hot_cosby.src.utils.etrade import get_etrade


class Huxtable(metaclass=abc.ABCMeta):
    """ Base type (family) for all hot-cosby component classes """

    collection: MongoCollections = NotImplemented

    class HistoryModel(BaseModel):
        timestamp: datetime.datetime
        cls: str
        event: dict

    def __init__(self):
        self.history = list()

        if self.collection is not None:
            self.mongo_client = mongo.get_client()

        self.etrade = get_etrade()

    def _handle_documents(self, documents):
        assert isinstance(documents, (dict, list))
        event = dict(method='_handle_documents', document_count=1 if isinstance(documents, dict) else len(documents))
        try:
            result = mongo.insert_document_data(
                client=self.mongo_client,
                collection=self.collection,
                document_data=documents
            )
            event['result'] = result
        except Exception as e:
            event['error'] = str(e)
            event['err_type'] = type(e).__name__
            event['result'] = result = 'Error'

        self.track_event(
            **event
        )

        return result

    def track_event(self, **event_data):
        self.history.append(
            self.HistoryModel(
                timestamp=datetime.datetime.now(),
                event=event_data,
                cls=self.__class__.__name__
            )
        )


from .claire import Claire
from .dabnis import Dabnis
from .denise import Denise
from .elvin import Elvin
from .heathclifford import HeathClifford
from kenny import Kenny
from olivia import Olivia
from rudith import Rudith
from sondra import Sondra
from theo import Theo
from vanessa import Vanessa


__all__ = ['Huxtable', 'Claire', 'Dabnis', 'Denise', 'Elvin', 'HeathClifford', 'Kenny',
           'Olivia', 'Rudith', 'Sondra', 'Theo', 'Vanessa']
