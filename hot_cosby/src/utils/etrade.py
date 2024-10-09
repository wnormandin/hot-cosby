import logging
from etrade_client.core.etrade import ETrade

logger = logging.getLogger(__name__)


def get_etrade():
    etrade = ETrade(use_cached_credentials=True)
    logger.info(f'Connected to {etrade}: {etrade.accounts[0]}')
    return etrade