#   0. * Add trace/debug/info/warning/error/critical methods to SimpleLogger. (optional)
#   1.  Make type hints for all methods.
#   2.  Implement base Connector class methods for MEXCConnector.
#   3.  Test MEXCConnector.
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

    expected_hash = 'e43468edbbddaba43b3b370658c76b594c5c0ddf729c96c9f7aa57892d0f05b4e7e504ca93d9a3c9745944ed693458419a65b01277d7b4e74635c4191dc70bb0'
    computed_hash = connector.get_exchange_info()
    assert computed_hash == expected_hash, f'Expected hash: {expected_hash}, Computed hash: {computed_hash}'
    logger.info('Exchange info is correct')

    input('Press Enter to continue...')
