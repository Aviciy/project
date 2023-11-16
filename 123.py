import json

import MEXC
from Abstract.connector import Connector
from Abstract.logger import Logger
from Loggers.composite_logger import CompositeLogger
from Loggers.console_logger import ConsoleLogger
from Loggers.file_logger import FileLogger

console_logger: Logger = ConsoleLogger()
file_logger: Logger = FileLogger('log.txt')
logger: Logger = CompositeLogger(console_logger, file_logger)

EXCHANGE_NAME = 'MEXC'

if __name__ == '__main__':
    with open('MEXC_settings.json', 'r') as file:
        settings = json.load(file)

    logger.debug(settings)

    connector: Connector = MEXC.Connector(logger, settings)
    connector.get_name()
    connector.check_connection()
    connector.get_balances()
input('Press Enter to continue...')
