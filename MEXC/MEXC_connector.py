import hashlib
import json

import requests
from requests import Response

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
        self.__base_url = "https://api.mexc.com"
        self.__logger.debug('MEXCConnector was created')

    def get_name(self) -> str:
        '''Returns the name of the exchange'''
        return 'MEXC'

    def check_connection(self) -> Response | bool:
        '''Checking the relevance of the connection'''
        try:
            self.__logger.debug('Checking connections')
            return requests.get(Endpoints.PING)
            # return requests.get(self.__make_endpoint(MEXCEndpoints.PING)).json()['PING'].ok
        except Exception as e:
            self.__logger.error(f'Connection error: {e} ')
            return False

    def get_server_time(self) -> int | None:
        try:
            response = requests.get(Endpoints.SERVER_TIME)
            if not response.ok:
                print(f'Error getting server time: {response.text}')
                return None
            server_time_data = response.json()
            server_time = server_time_data.get('serverTime')
            return server_time
        except Exception as e:
            print(f'Error getting server time: {e}')
            return None

    def get_exchange_info(self) -> [str]:
        try:
            response = requests.get(Endpoints.EXCHANGE_INFO).json()
            exchange_symbols = [item['symbol'] for item in response['symbols']]
            sorted_exchange_info = ', '.join(sorted(exchange_symbols))
            computed_hash = hashlib.sha512(sorted_exchange_info.encode()).hexdigest()
            return computed_hash
        except Exception as e:
            print(f'Error getting exchange info: {e}')
            return ''

    def get_ticker(self, symbol: str) -> float:
        '''Returns information about the Symbol'''
        self.__logger.debug('Return ticker')
        responce = requests.get(Endpoints.TICKER).json()
        _ticker = responce.json()

    def get_book(self, symbol: str) -> dict | None:
        '''Returns  book ticker'''
        self.__logger.debug('Return book')
        responce = requests.get(Endpoints.BOOK_TICKER).json()
        _book = responce.json()
        return

    def get_balances(self) -> dict | None:
        '''Returns balance information'''
        self.__logger.debug('Return balance data')
        responce = requests.get(Endpoints.BALANCES).json()
        _balance = responce.json()
        return

    def start(self) -> object:
        if not self.check_connection():
            self.__logger.error('Connection to MEXC failed.')
            return
        self.__logger.info('MEXC-Connector started')

    def on_event(self, broker_event: object, details: object) -> None:
        print('--- {}-{}-{}'.
              format(self,
                     broker_event,
                     details
                     )
              )

    def __make_endpoint(self, endpoint: str) -> str:
        return f"{self.__base_url}{endpoint}"

    def top_parse(self, message: str) -> None:
        msg = json.loads(message)
        md = msg['d']
        data = {'bid': float(md['b']), 'ask': float(md['a']), 'bidSize': float(md['B']), 'askSize': float(md['A']), 'symbol': msg['s'], 'ts': msg['t']}

        self.__callback(self.__instance_name, data['symbol'], data)

    def __callback(self, __instance_name, param, data):
        pass
