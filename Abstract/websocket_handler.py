from abc import ABCMeta, abstractmethod

from websocket import WebSocketApp


class WebSocketHandler(metaclass=ABCMeta):
    __metadata__ = ABCMeta

    def __init__(self) -> None:
        pass

    def on_message(self, ws: WebSocketApp, message: str) -> None:
        """Called when a message is received"""
        raise NotImplementedError

    def on_error(self, ws: WebSocketApp, error: Exception) -> None:
        """Called when an error occurs"""
        raise NotImplementedError

    def on_close(self, ws: WebSocketApp, close_status_code: int or str, close_msg: str) -> None:
        """Called when the connection is closed"""
        raise NotImplementedError

    def on_open(self, ws: WebSocketApp) -> None:
        """Called when the connection is opened"""
        raise NotImplementedError
