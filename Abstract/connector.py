from abc import ABCMeta, abstractmethod


class Connector(metaclass=ABCMeta):
    __metadata__ = ABCMeta

    def __init__(self) -> None:
        pass

    @abstractmethod
    def get_name(self) -> str:
        """Returns the name of the exchange"""
        raise NotImplementedError

    @abstractmethod
    def check_connection(self) -> bool:
        """Checking the relevance of the connection"""
        raise NotImplementedError

    @abstractmethod
    def get_server_time(self) -> int | None:
        """returning the server time"""
        raise NotImplementedError

    @abstractmethod
    def get_exchange_info(self) -> [str] or None:
        """Resolve get exchange symbols"""
        raise NotImplementedError

    @abstractmethod
    def get_ticker(self, symbol: str) -> dict | None:
        """return current symbol market price"""
        raise NotImplementedError

    @abstractmethod
    def get_book(self, symbol: str) -> dict | None:
        """Returns order book"""
        raise NotImplementedError

    @abstractmethod
    def get_balances(self) -> object | None:
        """Returns balance information"""
        raise NotImplementedError


class Stream(metaclass=ABCMeta):
    __metadata__ = ABCMeta

    @abstractmethod
    def subscribe_to_stream(self, subscriber, symbol, model, func):
        raise NotImplementedError

    # @abstractmethod
    # def unsubscribe(self, subscriber, symbol, model):
    #     raise NotImplementedError
