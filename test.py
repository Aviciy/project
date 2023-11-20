import json
import time

from websocket import WebSocketApp

import MEXC
from Abstract.connector import Connector
from Abstract.logger import Logger
from Abstract.websocket_handler import WebSocketHandler
from Loggers.composite_logger import CompositeLogger
from Loggers.console_logger import ConsoleLogger
from Loggers.file_logger import FileLogger


class LoggingWebSocketHandler(WebSocketHandler):

    def __init__(self, logger: Logger):
        super().__init__()
        self.__logger = logger

    def on_message(self, ws: WebSocketApp, message: str) -> None:
        self.__logger.debug(f'Message received: {message}')

    def on_error(self, ws: WebSocketApp, error: Exception) -> None:
        self.__logger.error(f'Error: {error}')

    def on_close(self, ws: WebSocketApp, close_status_code: int or str, close_msg: str) -> None:
        self.__logger.info(f'Closed: {close_status_code} {close_msg}')

    def on_open(self, ws: WebSocketApp) -> None:
        self.__logger.info('Opened')


console_logger: Logger = ConsoleLogger()
file_logger: Logger = FileLogger('log.txt')
composite_logger: Logger = CompositeLogger(console_logger, file_logger)

EXCHANGE_NAME = 'MEXC'

if __name__ == '__main__':
    with open('MEXC_settings.json', 'r') as file:
        settings = json.load(file)

    composite_logger.debug(settings)

    connector: Connector = MEXC.Connector(composite_logger, LoggingWebSocketHandler(composite_logger), settings)

    assert connector.start() is True, 'Start error'

    assert connector.get_name() == EXCHANGE_NAME, 'Wrong exchange name'
    composite_logger.info('Exchange name is correct')

    assert connector.check_connection(), 'Connection error'
    composite_logger.info('Check connection is correct')

    server_time = connector.get_server_time()
    current_time = int(time.time() * 1000)
    assert server_time is not None and abs(server_time - current_time) < 2 ** 16, 'Server time error'
    composite_logger.info(f'Server time is correct: delta = abs({server_time} - {current_time}) < {2 ** 16}ms')

    exchange_info = connector.get_exchange_info()
    assert exchange_info is not None and len(exchange_info) > 0, 'Exchange info error'
    composite_logger.info('Exchange info is correct')

    assert connector.get_ticker('BTCUSDT') is not None, 'Ticker error'
    composite_logger.info('Ticker is correct')

    assert connector.get_book('BTCUSDT') is not None, 'Book error'
    composite_logger.info('Book is correct')

    balances = connector.get_balances()
    assert balances is not None, 'Balance error'
    composite_logger.info(f'balances: {balances}')

    assert connector.subscribe('LTCUSDT'), 'LTCUSDT subscribe error'
    assert connector.subscribe('BTCUSDT'), 'BTCUSDT subscribe error'

    input()

    assert connector.stop() is True, 'Stop error'

    print("ALL DONE")

input('Press Enter to continue...')
