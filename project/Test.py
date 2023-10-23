import logging.config
import time

from sortedcontainers import SortedDict

from MEXCWrapper import MEXCWrapper


if __name__ == "__main__":

    def on_market_top(instance_name, coin, top):
        pass

    def on_market_book(instance_name, coin, book):
        pass

    def on_event(exchange_name, broker_event, details=""):
        print('--- {}-{}-{}'.
              format(exchange_name,
                     broker_event,
                     details
                     )
              )

    settingsMEXC = {
        'key': 'mx0aBYs33eIilxBWC5',
        'secret': '45d0b3c26f2644f19bfb98b07741b2f5',
        'url': 'wbs.mexc.com',
        'wss': 'wss://wbs.mexc.com/ws',
        'type_of_full_subscription': 'orderBookL2',
        'warning_delay_sec': '5',
        'maximum_delay_sec': '25'
    }
   