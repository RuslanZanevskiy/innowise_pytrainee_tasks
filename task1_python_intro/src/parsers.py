import sys

import logging

from dotenv import dotenv_values

logger = logging.getLogger(__name__)


class DbConfigParser:
    @staticmethod
    def parse_config(envfile: str = '.env') -> dict:
        logger.info(f'parsing db config from {envfile}')
        config = dotenv_values(envfile)
        config.setdefault('port', '5432')
        config.setdefault('host', 'localhost')

        assert set(config.keys()) == {'database', 'user', 'password', 'host', 'port'}

        return config

class ArgumentParser:
    @staticmethod
    def parse_args(nargs=-1) -> tuple:
        logger.info('parsing arguments')
        args = sys.argv[1:]
        if nargs != -1:
            assert len(args) == nargs
        return tuple(args)
