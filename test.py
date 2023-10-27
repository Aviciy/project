#   1.  *Move connector settings from .py file to .json file.
#   2.  *Make doc strings for all methods.
#   3.  *Make type hints for all methods.
#   4.  *Implement your own simple logging system. (print to console and write to file)
#   5.  Implement connector for MEXC exchange.
#   6.  Test your connector.
import json

from MEXC.mexcconnector import MEXCConnector
from Shared.logger import logger

with open('MEXC_settings.json', 'r') as file:
    settings = json.load(file)

logger.debug(settings)
connector = MEXCConnector(logger, settings)
