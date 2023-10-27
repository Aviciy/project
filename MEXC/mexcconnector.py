from abc import abstractmethod

import requests

from Shared.connector import Connector
from Shared.logger import SimpleLogger


class MEXCConnector(Connector):

    def __init__(self, logger: SimpleLogger, settings: dict) -> None:
        super().__init__()
        self.__server = None
        self.__logger = logger
        self.__settings = settings
        self.__base_url = "https://api.mexc.com"
        self.__logger.debug('MEXCConnector was created')

    def __make_endpoint(self, endpoint: str) -> str:
        return f"{self.__base_url}{endpoint}"

    @abstractmethod
    def get_name(self) -> str:
        '''Returns the name of the exchange'''
        return 'MEXC'

    @abstractmethod
    def check_connection(self) -> bool:
        '''Checking the relevance of the connection'''
        try:
            self.__logger.debug('Checking connections')
            return requests.get(self.__make_endpoint('/api/v3/ping')).ok
        except Exception as e:
            self.__logger.error(f'Connection error: {e} ')
            return False

    @abstractmethod
    def get_server_time(self) -> None:
        '''returning the server time'''
        self.__logger.debug('Checking server time')
        responce = requests.get('/api/v3/time')
        _server_time = responce.json()
        return

    @abstractmethod
    def get_exchange_info(self) -> None:
        '''Returns the exchange data'''
        self.__logger.debug('Get exchange info')
        responce = requests.get('/api/v3/exchangeInfo')
        _exchange_info = responce.json()
        return

    @abstractmethod
    def get_ticker(self, symbol: str) -> object:
        '''Returns information about the Symbol'''
        self.__logger.debug('Return ticker')
        responce = requests.get('/api/v3/ticker')
        _ticker = responce.json()
        return

    @abstractmethod
    def get_book(self, symbol: str) -> object:
        '''Returns  book ticker'''
        self.__logger.debug('Return book')
        responce = requests.get('/api/v3/ticker/bookTicker')
        _book = responce.json()
        return

    @abstractmethod
    def get_balances(self) -> object :
        '''Returns balance information'''
        self.__logger.debug('Return balance data')
        responce = requests.get('/api/v3/capital/config/getall')
        _balance = responce.json()
        return
