import logging

from .. import Huxtable
from hot_cosby.src.db import get_session
from hot_cosby.src.db.crud import get_config, set_config


logger = logging.getLogger(__name__)


class Kenny(Huxtable):
    """
    Kenny is not truly a Huxtable, cannot be run asynchronously due to the required user input step in the authorization
    process.  User auth is good for 24 hours and so regular user interactions are necessary to maintain the process
    """

    @property
    def code_is_set(self):
        session = get_session()
        try:
            return get_config(session=session, key='USER_CODE') is not None
        finally:
            session.close()

    def check_current_auth(self):
        try:
            self.etrade.client.list_accounts()
        except Exception as e:
            logger.warning(f'Error attempting to test auth: {str(e)}')
            self.etrade.client.authenticate()
            assert self.etrade.client.verifier is not None
            self.set_current_auth()
            self.track_event(method='check_current_auth', result='reauthenticated')
        else:
            self.track_event(method='check_current_auth', result='success')

    def set_current_auth(self):
        session = get_session()
        try:
            return set_config(session=session, key='USER_CODE', value=self.etrade.client.verifier)
        finally:
            session.close()


__all__ = ['Kenny']
