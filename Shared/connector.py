from abc import ABCMeta, abstractmethod, abstractproperty


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
        raise NotImplementedError

    @abstractmethod
    def get_server_time(self):
        raise NotImplementedError

    @abstractmethod
    def get_exchange_info(self):
        raise NotImplementedError

    @abstractmethod
    def get_ticker(self, symbol):
        raise NotImplementedError

    @abstractmethod
    def get_book(self, symbol):
        raise NotImplementedError

    @abstractmethod
    def get_balances(self):
        raise NotImplementedError
