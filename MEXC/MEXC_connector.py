import json

import requests

from MEXC.MEXC_endpoints import MEXCEndpoints
from Shared.connector import Connector
from Shared.logger import SimpleLogger


class MEXCConnector(Connector):

    def __init__(self, logger: SimpleLogger, settings: dict) -> None:
        super().__init__()
        self.__instance_name = None
        self.__server = None
        self.__logger = logger
        self.__settings = settings
        self.__base_url = "https://api.mexc.com"
        self.__logger.debug('MEXCConnector was created')

    def on_event(exchange_name, broker_event: object, details: object = "") -> object:
        print('--- {}-{}-{}'.
              format(exchange_name,
                     broker_event,
                     details
                     )
              )

    def __make_endpoint(self, endpoint: str) -> str:
        return f"{self.__base_url}{endpoint}"

    def get_name(self) -> str:
        '''Returns the name of the exchange'''
        return 'MEXC'

    def check_connection(self) -> bool:
        '''Checking the relevance of the connection'''
        try:
            self.__logger.debug('Checking connections')
            return requests.get(MEXCEndpoints.PING)
            # return requests.get(self.__make_endpoint(MEXCEndpoints.PING)).json()['PING'].ok
        except Exception as e:
            self.__logger.error(f'Connection error: {e} ')
            return False

    def get_server_time(self) -> int | None:
        '''returning the server time'''
        self.__logger.debug('Return server time')
        try:
            return requests.get(MEXCEndpoints.SERVER_TIME).json()['SERVER_TIME']
        except Exception as e:
            self.__logger.error(f'Error getting server time: {e}')
            raise e

    def get_exchange_info(self) -> [str]:
        '''Returns the exchange data'''
        self.__logger.debug('Get exchange info')
        responce = requests.get(MEXCEndpoints.EXCHANGE_INFO).json()
        _exchange_info = responce.json()
        return

    def get_ticker(self, symbol: str) -> float:
        '''Returns information about the Symbol'''
        self.__logger.debug('Return ticker')
        responce = requests.get(MEXCEndpoints.TICKER).json()['TICKER']
        _ticker = responce.json()

    def get_book(self, symbol: str) -> dict:
        '''Returns  book ticker'''
        self.__logger.debug('Return book')
        responce = requests.get(MEXCEndpoints.BOOK_TICKER).json()['BOOK_TICKER']
        _book = responce.json()
        return

    def get_balances(self) -> dict:
        '''Returns balance information'''
        self.__logger.debug('Return balance data')
        responce = requests.get(MEXCEndpoints.BALANCES).json()['BALANCES']
        _balance = responce.json()
        return

    def subscribe(self: object, symbol: str, type: object) -> float:
        subscription = {
            "method": "SUBSCRIPTION",
            "params": ["spot@public.deals.v3.api@BTCUSDT"]
        }

        json.dumps(subscription)

    def unsubscribe(self: object, symbol: str, type: object) -> float:
        unsubscription = {
            "method": "UNSUBSCRIPTION",
            "params": ["spot@public.deals.v3.api@BTCUSDT", "spot@public.increase.depth.v3.api@BTCUSDT"]
        }

        json.dumps(unsubscription)

    def top_parse(self, message: object) -> float:
        msg = json.loads(message)
        md = msg['d']
        data = {}
        data['bid'] = float(md['b'])
        data['ask'] = float(md['a'])
        data['bidSize'] = float(md['B'])
        data['askSize'] = float(md['A'])
        data['symbol'] = msg['s']
        data['ts'] = msg['t']

        self.__callback(self.__instance_name, data['symbol'], data)

    def __callback(self, __instance_name, param, data):
        pass

    def start(self) -> object:
        if not self.check_connection():
            self.__logger.error('Connection to MEXC failed.')
            return
        self.__logger.info('MEXC-Connector started')
