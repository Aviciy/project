import requests

import MEXC
from Abstract.connector import Connector
from Loggers.logger_setup import composite_logger, settings
from MEXC.LoggingWebSocket import LoggingWebSocketHandler

EXCHANGE_NAME = 'MEXC'

if __name__ == '__main__':
    composite_logger.debug(settings)

    connector: Connector = MEXC.Connector(composite_logger, LoggingWebSocketHandler(composite_logger), settings)

    # assert connector.start() is True, 'Start error'
    #
    # assert connector.get_name() == EXCHANGE_NAME, 'Wrong exchange name'
    # composite_logger.info('Exchange name is correct')
    #
    # assert connector.check_connection(), 'Connection error'
    # composite_logger.info('Check connection is correct')
    #
    # server_time = connector.get_server_time()
    # current_time = int(time.time() * 1000)
    # assert server_time is not None and abs(server_time - current_time) < 2 ** 16, 'Server time error'
    # composite_logger.info(f'Server time is correct: delta = abs({server_time} - {current_time}) < {2 ** 16}ms')
    #
    # exchange_info = connector.get_exchange_info()
    # assert exchange_info is not None and len(exchange_info) > 0, 'Exchange info error'
    # composite_logger.info('Exchange info is correct')
    #
    # assert connector.get_ticker('BTCUSDT') is not None, 'Ticker error'
    # composite_logger.info('Ticker is correct')
    #
    # assert connector.get_book('BTCUSDT') is not None, 'Book error'
    # composite_logger.info('Book is correct')
    #
    # balances = connector.get_balances()
    # assert balances is not None, 'Balance error'
    # composite_logger.info(f'balances: {balances}')
    #
    # assert connector.subscribe('BTCUSDT'), 'BTCUSDT subscribe error'
    #
    # time.sleep(5)
    # assert connector.unsubscribe('BTCUSDT'), 'BTCSUDT connection close'
    #
    # assert connector.stop() is True, 'Stop error'
    #
    # connector.test_order()
    # connector.make_order()
    # connector.batch_order()
    # connector.cancel_order()
    # connector.cancel_all_order()
    connector.order_book()

input('Press Enter to continue...')
