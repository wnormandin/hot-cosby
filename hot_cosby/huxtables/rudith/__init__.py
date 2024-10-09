import logging

import click_log

from .. import Huxtable
from ..kenny import Kenny
import click
from click_log import basic_config


logger = logging.getLogger(__name__)
basic_config(logger)


class Rudith(Huxtable):
    def __init__(self):
        super().__init__()
        self.auth = Kenny()
        self.track_event(method='__init__')

    @click.group('rudy')
    @click_log.simple_verbosity_option
    @click.pass_context
    def cli(self, ctx):
        """ Entry point for CLI activities """
        ctx.ensure_object(dict)
        self.auth.check_current_auth()

    @cli.command()
    @click.pass_context
    def authenticate(self, ctx):
        """ Leverages Kenny for managing eTrade authentication """
        # TODO: on-demand reauthentication

    @cli.command()
    @click.pass_context
    def status(self, ctx):
        """ Heartbeat/status checks on the core hot cosby services (Uses Dabnis REST API) """
        # TODO: mongo/postgres queries, celery subsystem checks


__all__ = ['Rudith']


if __name__ == '__main__':
    rudith = Rudith()
    rudith.cli()
