from abc import abstractmethod

from Shared.connector import Connector
from Shared.logger import SimpleLogger


class MEXCConnector(Connector):

    def __init__(self, logger: SimpleLogger, settings: dict) -> None:
        self.__logger = logger
        self.__settings = settings
        self.__logger.debug('MEXCConnector was created')

    @abstractmethod
    def get_name(self) -> str:
        '''Returns the name of the exchange'''
        raise NotImplementedError

    @abstractmethod
    def check_connection(self) -> bool:
        '''Checking the relevance of the connection'''
        raise NotImplementedError

    @abstractmethod
    def get_server_time(self) -> str:
        '''returning the server time'''
        raise NotImplementedError

    @abstractmethod
    def get_exchange_symbols(self) -> [str]:
        '''Returns the exchange data'''
        raise NotImplementedError

    @abstractmethod
    def get_ticker(self, symbol: str) -> dict:
        '''Returns information about the Symbol'''
        raise NotImplementedError

    @abstractmethod
    def get_book(self, symbol: str) -> dict:
        '''Returns order book'''
        raise NotImplementedError

    @abstractmethod
    def get_balances(self) -> dict:
        '''Returns balance information'''
        raise NotImplementedError
