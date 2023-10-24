from abc import ABCMeta, abstractmethod, abstractproperty


class IConnector(object):
    __metadata__ = ABCMeta

    def __init__(self):
        pass

    # market channel
    @abstractmethod
    def subscribe(self, subscriber, symbol, model, func):
        raise NotImplementedError

    @abstractmethod
    def unsubscribe(self, subscriber, symbol, model):
        raise NotImplementedError

    @abstractmethod
    def get_ticker(self, market):
        raise NotImplementedError

    @abstractmethod
    def get_book(self, market):
        raise NotImplementedError

    # trade channel
    @abstractmethod
    def send(self, details):
        raise NotImplementedError

    @abstractmethod
    def cancel(self, details):
        raise NotImplementedError

    @abstractmethod
    def modify(self, details):
        raise NotImplementedError

    @abstractmethod
    def balances(self):
        raise NotImplementedError

    @abstractmethod
    def start(self, details):
        raise NotImplementedError

    @abstractmethod
    def stop(self):
        raise NotImplementedError

    @abstractmethod
    def get_position(self, market):
        raise NotImplementedError

    @abstractproperty
    def name(self):
        raise NotImplementedError

    @abstractproperty
    def is_connected(self):
        raise NotImplementedError

    @abstractproperty
    def is_started(self):
        raise NotImplementedError