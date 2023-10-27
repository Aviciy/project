from abc import ABCMeta, abstractmethod

class Connector(object):
    __metadata__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def get_name(self):
        '''Returns the name of the exchange'''
        raise NotImplementedError

    @abstractmethod
    def check_connection(self):
        '''Checking the relevance of the connection'''
        raise NotImplementedError

    @abstractmethod
    def get_server_time(self):
        '''returning the server time'''
        raise NotImplementedError

    @abstractmethod
    def get_exchange_info(self):
        '''Returns the exchange data'''
        raise NotImplementedError

    @abstractmethod
    def get_ticker(self, symbol):
        '''Returns information about the Symbol'''
        raise NotImplementedError

    @abstractmethod
    def get_book(self, symbol):
        '''Returns order book'''
        raise NotImplementedError

    @abstractmethod
    def get_balances(self):
        '''Returns balance information'''
        raise NotImplementedError