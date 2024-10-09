import logging
from pymongo import MongoClient
from typing import Union
from ..config import MONGO_HOST, MONGO_PORT
from ..config.globals import MongoCollections


logger = logging.getLogger(__name__)


def get_client(host: str = None, port: int = None) -> MongoClient:
    return MongoClient(host=host or MONGO_HOST, port=port or MONGO_PORT)


def create_collections(client: MongoClient) -> None:
    for collection in MongoCollections:
        client.create_collection(collection.value)


def insert_document_data(
        client: MongoClient,
        document_data: Union[dict, list],
        collection: MongoCollections = MongoCollections.quotes,
        strict: bool = True
        ) -> Union[int, list, bool]:
    """
    Inserts one or many documents to the given collection based on the type of the passed document_data variable

    :param client: An instance of the MongoClient class
    :param document_data: A dict or list containing the documents to be inserted
    :param collection: A MongoCollection enum instance indicating the target collection
    :param strict: A boolean flag indicating whether to raise an exception when errors are encountered
    :return: If given a single dict in document_data, the inserted document ID will be returned.
             If given multiple dicts in document_data, the inserted docuemnt IDs will be returned as a list.
             If an exception is encountered, returns False after logging the exception details unless the strict param
               is True
    """

    coll = client[collection.value]
    try:
        if isinstance(document_data, dict):
            return coll.insert_one(document_data)
        else:
            return coll.insert_many(document_data)
    except Exception as e:
        logger.warning(f'Error inserting document data: {document_data}')
        logger.error(str(e))
        if strict:
            raise
        return False


__all__ = ['get_client', 'insert_document_data']
