import json
import time

import MEXC
from Abstract.connector import Connector
from Abstract.logger import Logger
from Loggers.composite_logger import CompositeLogger
from Loggers.console_logger import ConsoleLogger
from Loggers.file_logger import FileLogger
from MEXC.MEXC_connector import Stream

console_logger: Logger = ConsoleLogger()
file_logger: Logger = FileLogger('log.txt')
logger: Logger = CompositeLogger(console_logger, file_logger)

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
    assert exchange_info is not None and len(exchange_info) > 0, 'Exchange info error'
    logger.info('Exchange info is correct')

    assert connector.get_ticker('BTCUSDT') is not None, 'Ticker error'
    logger.info('Ticker is correct')

    assert connector.get_book('BTCUSDT') is not None, 'Book error'
    logger.info('Book is correct')

    # assert connector.get_balances() is not None, 'Balance error'
    # logger.info('Balance is correct')
    balances = connector.get_balances()
    assert balances is not None, 'Balance error'
    logger.info(f'balances: {balances}')

    your_instance = Stream()
    your_instance.subscribe_to_stream()

input('Press Enter to continue...')
