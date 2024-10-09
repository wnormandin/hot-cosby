"""
Vanessa Huxtable fetches quote data from the eTrade REST API based on the quotes
"""

from hot_cosby.src.config.globals import MongoCollections
from ...huxtables import Huxtable


class Vanessa(Huxtable):
    collection = MongoCollections.quotes

    def __init__(self):
        super().__init__()
        self.pending_quotes = list()

    async def pull_quotes(self):
        """ Pull quotes based on the pending symbol list"""
        # TODO: get symbols from redis
        symbols = []
        self.pending_quotes.extend(self.etrade.get_quotes(symbols=symbols))
        await self.push_documents()

    async def push_documents(self):
        """ Push currently stored quotes to Mongodb """
        self._handle_documents(self.pending_quotes)
        self.pending_quotes = list()


__all__ = ['Vanessa']
