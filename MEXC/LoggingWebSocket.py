import json

from websocket import WebSocketApp

from Abstract.logger import Logger
from Abstract.websocket_handler import WebSocketHandler


class LoggingWebSocketHandler(WebSocketHandler):

    def __init__(self, logger: Logger):
        super().__init__()
        self.__logger = logger

    def on_message(self, ws: WebSocketApp, message: str) -> None:
        data = json.loads(message)
        if 's' in data and 'd' in data:
            symbol = data['s']
            price = data['d']['deals'][0]['p']
            output_message = f'"{symbol}" ->  {price}'
            self.__logger.debug(output_message)

    def on_error(self, ws: WebSocketApp, error: Exception) -> None:
        self.__logger.error(f'Error: {error}')

    def on_close(self, ws: WebSocketApp, close_status_code: int or str, close_msg: str) -> None:
        status_code_str = str(close_status_code) if close_status_code is not None else ''
        message_str = str(close_msg) if close_msg is not None else ''

        self.__logger.info(f'Closed: {status_code_str} {message_str}' if status_code_str or message_str else 'Closed: No status code or message')

    def on_open(self, ws: WebSocketApp) -> None:
        self.__logger.info('Opened')
