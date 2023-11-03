#   0. * Add trace/debug/info/warning/error/critical methods to SimpleLogger. (optional)
#   1.  Make type hints for all methods.
#   2.  Implement base Connector class methods for MEXCConnector.
#   3.  Test MEXCConnector.
import hashlib
import json
import time

import MEXC
from Shared.connector import Connector
from Shared.logger import logger

EXCHANGE_NAME = 'MEXC'

if __name__ == '__main__':
    with open('MEXC_settings.json', 'r') as file:
        settings = json.load(file)

    logger.debug(settings)

    connector: Connector = MEXC.Connector(logger, settings)

    assert connector.get_name() == EXCHANGE_NAME, 'Wrong exchange name'
    logger.info('Exchange name is correct')

    assert connector.check_connection(), 'Connection error'
    logger.info('Check connection is correct')

    server_time = connector.get_server_time()
    current_time = int(time.time() * 1000)
    assert server_time is not None and abs(server_time - current_time) < 2 ** 16, 'Server time error'
    logger.info(f'Server time is correct: delta = abs({server_time} - {current_time}) < {2 ** 16}ms')

    exchange_info = connector.get_exchange_info()
    assert hashlib.sha512(str.encode(', '.join(sorted(exchange_info)))).hexdigest() == \
           '28a90e53cb087356a5c5ca6d54d576736c0f5232c6177904076963f88773639468ea4c63a661c20396822bd36b07bf22dd6a0d3407e4d408d57d0ca2dba8449b', 'Exchange info error'
    logger.info('Exchange info is correct')

    input('Press Enter to continue...')
