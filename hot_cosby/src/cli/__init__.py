import logging
import click
import click_log


logger = logging.getLogger(__name__)
click_log.basic_config(logger=logger)


@click.group()
def cli():
    """ CLI Entry point """
