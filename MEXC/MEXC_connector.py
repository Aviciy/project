import json

import requests

from MEXC import Endpoints
from Shared.connector import Connector
from Shared.logger import SimpleLogger


def subscribe() -> None:
    subscription = {
        "method": "SUBSCRIPTION",
        "params": ["spot@public.deals.v3.api@BTCUSDT"]
    }

    json.dumps(subscription)


def unsubscribe() -> None:
    unsubscription = {
        "method": "UNSUBSCRIPTION",
        "params": ["spot@public.deals.v3.api@BTCUSDT", "spot@public.increase.depth.v3.api@BTCUSDT"]
    }

    json.dumps(unsubscription)


class MEXCConnector(Connector):

    def __init__(self, logger: SimpleLogger, settings: dict) -> None:
        super().__init__()
        self.__instance_name = None
        self.__server = None
        self.__logger = logger
        self.__settings = settings

        self.__logger.trace('MEXCConnector was created')

    def get_name(self) -> str:
        """Returns the name of the exchange"""
        return 'MEXC'

    def check_connection(self) -> bool:
        """Checking the relevance of the connection"""
        try:
            self.__logger.trace('Checking connection')
            return requests.get(Endpoints.PING).ok
            # return requests.get(self.__make_endpoint(MEXCEndpoints.PING)).json()['PING'].ok
        except Exception as e:
            self.__logger.error(f'Connection error: {e} ')
            return False

    def get_server_time(self) -> int | None:
        try:
            response = requests.get(Endpoints.SERVER_TIME)
            if not response.ok:
                self.__logger.error(f'Error getting server time: {response.text}')
                return None
            server_time_data = response.json()
            server_time = server_time_data.get('serverTime')
            return server_time
        except Exception as e:
            self.__loger.error(f'Error getting server time: {e}')
            return None

    def get_ticker(self, symbol: str) -> float | None:
        """Returns information about the Symbol"""
        try:
            self.__logger.trace('Return ticker')
            response = requests.get(Endpoints.TICKER).json()
            _ticker = response
            return _ticker
        except Exception as e:
            self.__logger.error(f'Error getting ticker: {e}')
            return None

    def get_exchange_info(self) -> [str] or None:
        try:
            response = requests.get(Endpoints.EXCHANGE_INFO).json()
            exchange_symbols = [item['symbol'] for item in response['symbols']]
            return exchange_symbols
        except Exception as e:
            self.__logger.error(f'Error getting exchange info: {e}')
            return None

    def get_book(self, symbol: str) -> dict | None:
        """Returns  book ticker"""
        try:
            self.__logger.trace('Return book')
            response = requests.get(Endpoints.BOOK_TICKER).json()
            _book = response

            return _book
        except Exception as e:
            self.__logger.error(f'Error getting book: {e}')
            return None

    def get_balances(self) -> dict | None:
        """Returns balance information"""
        try:
            self.__logger.trace('Return balance data')
            response = requests.get(Endpoints.BALANCES).json()
            return response
        except Exception as e:
            self.__logger.error(f'Error getting balance info: {e}')
            return None

    def start(self) -> bool:
        if not self.check_connection():
            self.__logger.error('Connection to MEXC failed.')
            return False
        self.__logger.info('MEXC-Connector started')
        return True

    def on_event(self, broker_event: object, details: object) -> None:
        print('--- {}-{}-{}'.
              format(self,
                     broker_event,
                     details
                     )
              )

    def top_parse(self, message: str) -> None:
        msg = json.loads(message)
        md = msg['d']
        data = {'bid': float(md['b']), 'ask': float(md['a']), 'bidSize': float(md['B']), 'askSize': float(md['A']), 'symbol': msg['s'], 'ts': msg['t']}

        self.__callback(self.__instance_name, data['symbol'], data)

    def __callback(self, __instance_name, param, data):
        pass
