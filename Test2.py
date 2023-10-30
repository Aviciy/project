import json

import requests

from MEXC.MEXC_connector import MEXCConnector
from Shared.logger import logger

with open('MEXC_settings.json', 'r') as file:
    settings = json.load(file)

if __name__ == '__main__':
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


    def get_ticker(self, symbol: str) -> object:
        '''Returns information about the Symbol'''
        self.__logger.debug('Return ticker')
        responce = requests.get('/api/v3/ticker')
        _ticker = responce.json()
        print(_ticker)
        return


    symbolMexc = {'first': 'XBT', 'second': 'USD', 'symbol': 'BNBUSDT'}
    currentSymbol = symbolMexc


class SubscriptionModel:
    TopBook = "TopBook"
    FullBook = "FullBook"
    Trade = "Trade"


logger.debug(settings)
connector = MEXCConnector(logger, settings)
connector.start()
connector.subscribe(symbolMexc, SubscriptionModel.TopBook)

input()
