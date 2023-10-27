#   0. * Add trace/debug/info/warning/error/critical methods to SimpleLogger. (optional)
#   1.  Make type hints for all methods.
#   2.  Implement base Connector class methods for MEXCConnector.
#   3.  Test MEXCConnector.
import json

from MEXC.mexcconnector import MEXCConnector
from Shared.logger import logger

with open('MEXC_settings.json', 'r') as file:
    settings = json.load(file)

logger.debug(settings)
connector = MEXCConnector(logger, settings)


def on_market_top(instance_name, coin, top):
    print('{}-{} top  Bid: {:f}({:f}) Ask: {:f}({:f})'.
          format(instance_name,
                 coin,
                 top['bid'],
                 top['bidSize'],
                 top['ask'],
                 top['askSize'],
                 )
          )
