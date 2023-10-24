import logging.config
import time

from Connector.MEXCWrapper import MEXCWrapper
from Declarations.models import SubscriptionModel

if __name__ == "__main__":

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

    def on_market_book(instance_name, coin, book):
        pass

    def on_event(exchange_name, broker_event, details=""):
        print('--- {}-{}-{}'.
              format(exchange_name,
                     broker_event,
                     details
                     )
              )

    def order_callback(name, report):
        pass

    

    settingsMEXC = {
        'key': 'mx0aBYs33eIilxBWC5',
        'secret': '45d0b3c26f2644f19bfb98b07741b2f5',
        'url': 'wbs.mexc.com',
        'wss': 'wss://wbs.mexc.com/ws',
        'type_of_full_subscription': 'orderBookL2',
        'warning_delay_sec': '5',
        'maximum_delay_sec': '25'
    }
    # depth10, depth

    symbolBitmex = {'first': 'XBT', 'second': 'USD', 'symbol': 'BNBUSDT'}
    

    currentSymbol = symbolBitmex

    logging.config.fileConfig('Connector/logger.cfg')

    __logger = logging.getLogger('MEXC')

    
    wrapper = MEXCWrapper(settingsMEXC, on_event)

    wrapper.start()
    time.sleep(3)

    wrapper.subscribe('client01', {'symbol': currentSymbol}, SubscriptionModel.TopBook, on_market_top)
    #time.sleep(1)
    #wrapper.subscribe('client02', {'symbol': currentSymbol}, SubscriptionModel.FullBook, on_market_book)

    input()