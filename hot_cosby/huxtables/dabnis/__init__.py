from fastapi import FastAPI
from .. import Huxtable


class Dabnis(Huxtable):
    def __init__(self):
        super().__init__()
        self.api = FastAPI()

    async def configure_basic_api(self):
        @self.api.get('/')
        async def heartbeat() -> dict:
            """ HTTP Heartbeat resource """

        @self.api.get('/config')
        async def get_config() -> dict:
            """ Retrieve the current hot cosby configuration from the PostGREs database """

        @self.api.post('/config/{key}')
        async def set_config(key: str) -> bool:
            """ Set a configuration value via JSON payload """


async def api_init():
    dabnis = Dabnis()
    await dabnis.configure_basic_api()


__all__ = ['Dabnis']


if __name__ == '__main__':
    import asyncio
    asyncio.run(api_init())
