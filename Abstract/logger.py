from abc import ABCMeta, abstractmethod


class Logger(metaclass=ABCMeta):
    __metadata__ = ABCMeta

    def __init__(self) -> None:
        pass

    @abstractmethod
    def trace(self, message: str) -> None:
        """Logs a message with level TRACE"""
        raise NotImplementedError

    @abstractmethod
    def debug(self, message: str) -> None:
        """Logs a message with level DEBUG"""
        raise NotImplementedError

    @abstractmethod
    def info(self, message: str) -> None:
        """Logs a message with level INFO"""
        raise NotImplementedError

    @abstractmethod
    def warning(self, message: str) -> None:
        """Logs a message with level WARNING"""
        raise NotImplementedError

    @abstractmethod
    def error(self, message: str) -> None:
        """Logs a message with level ERROR"""
        raise NotImplementedError

    @abstractmethod
    def critical(self, message: str) -> None:
        """Logs a message with level CRITICAL"""
        raise NotImplementedError
