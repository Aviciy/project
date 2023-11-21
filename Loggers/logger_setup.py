import json

from Abstract.logger import Logger
from Loggers.composite_logger import CompositeLogger
from Loggers.console_logger import ConsoleLogger
from Loggers.file_logger import FileLogger

console_logger: Logger = ConsoleLogger()
file_logger: Logger = FileLogger('log.txt')
composite_logger: Logger = CompositeLogger(console_logger, file_logger)

with open('MEXC_settings.json', "r") as file:
    settings = json.load(file)
