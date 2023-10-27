from abc import ABCMeta, abstractmethod

class Connector(object):
    __metadata__ = ABCMeta

    def __init__(self)-> None:
        pass

    @abstractmethod
    def get_name(self)-> str:
        '''Returns the name of the exchange'''
        raise NotImplementedError

    @abstractmethod
    def check_connection(self)-> bool:
        '''Checking the relevance of the connection'''
        raise NotImplementedError

    @abstractmethod
    def get_server_time(self)-> str:
        '''returning the server time'''
        raise NotImplementedError

    @abstractmethod
    def get_exchange_info(self)-> dict:
        '''Returns the exchange data'''
        raise NotImplementedError

    @abstractmethod
    def get_ticker(self, symbol:str)-> dict:
        '''Returns information about the Symbol'''
        raise NotImplementedError

    @abstractmethod
    def get_book(self, symbol:str)-> dict:
        '''Returns order book'''
        raise NotImplementedError

    @abstractmethod
    def get_balances(self)-> dict:
        '''Returns balance information'''
        raise NotImplementedError