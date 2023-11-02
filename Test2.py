import json

import requests

from MEXC.MEXC_connector import MEXCConnector
from MEXC.MEXC_endpoints import MEXCEndpoints
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

request = requests.get(MEXCEndpoints.PING).text
# subscribe = connector.subscribe(symbolMexc, SubscriptionModel.TopBook)
# time.sleep(3)
server_time = requests.get(MEXCEndpoints.SERVER_TIME).text
exchange_info = requests.get(MEXCEndpoints.EXCHANGE_INFO).json()
ticker = requests.get(MEXCEndpoints.TICKER).json()
book = requests.get(MEXCEndpoints.BOOK_TICKER).json()
# balance = requests.get(MEXCEndpoints.BALANCES).json()

connector.start()
# V1
# while True:
# ticker = requests.get(MEXCEndpoints.TICKER).json()
# decired_symbol = 'BTCUSDT'
# for item in ticker:
# if item['symbol'] == decired_symbol:
# decired_price = item['price']
# print(f'{decired_symbol}:{decired_price}')
# time.sleep(5)

# V2
# while True:
#   book = requests.get(MEXCEndpoints.BOOK_TICKER).json()
#  decired_symbol = 'BTCUSDT'
# for item in book:
#    bid_price = item['bidPrice']
#   ask_price = item['askPrice']
#  print(f'{decired_symbol}:"BidPrice" {bid_price} "AskPrice" {ask_price}')
# time.sleep(5)
print(exchange_info)
input()
