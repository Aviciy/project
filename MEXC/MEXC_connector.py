import hashlib
import hmac
import json
import time
from urllib.parse import urlencode

import requests
from self import self
from websocket._app import WebSocketApp

from Abstract.connector import Connector
from Abstract.logger import Logger
from MEXC import Endpoints


class MEXCConnector(Connector):

    def __init__(self, logger: Logger, settings: dict) -> None:
        super().__init__()
        self.__instance_name = None
        self.__server = None
        self.__logger = logger
        self.__settings = settings

        self.__logger.trace('MEXCConnector was created')

    def get_name(self) -> str:
        return 'MEXC'

    def check_connection(self) -> bool:
        try:
            self.__logger.trace('Checking connection')
            return requests.get(Endpoints.PING).ok
        except Exception as e:
            self.__logger.error(f'Connection error: {e} ')
            return False

    def get_server_time(self) -> int | None:
        try:
            response = requests.get(Endpoints.SERVER_TIME)
            if not response.ok:
                self.__logger.error(f'Error getting server time: {response.text}')
                return None
            server_time_data = response.json()
            server_time = server_time_data.get('serverTime')
            return server_time
        except Exception as e:
            self.__logger.error(f'Error getting server time: {e}')
            return None

    def get_ticker(self, symbol: str) -> dict | None:
        try:
            self.__logger.trace('Return ticker')
            response = requests.get(Endpoints.TICKER).json()
            _ticker = response
            return _ticker
        except Exception as e:
            self.__logger.error(f'Error getting ticker: {e}')
            return None

    def get_exchange_info(self) -> [str] or None:
        try:
            response = requests.get(Endpoints.EXCHANGE_INFO).json()
            exchange_symbols = [item['symbol'] for item in response['symbols']]
            return exchange_symbols
        except Exception as e:
            self.__logger.error(f'Error getting exchange info: {e}')
            return None

    def get_book(self, symbol: str) -> dict | None:
        try:
            self.__logger.trace('Return book')
            response = requests.get(Endpoints.BOOK_TICKER).json()
            _book = response

            return _book
        except Exception as e:
            self.__logger.error(f'Error getting book: {e}')
            return None

    def get_balances(self) -> object | None:
        try:
            self.__logger.trace('Return balance data')
            response = self.__make_signed_request(Endpoints.BALANCES, 'get').json()
            return response
        except Exception as e:
            self.__logger.error(f'Error getting balance info: {e}')
            return None

    def __make_signed_request(self, url: str, method: str, **kwargs) -> dict:
        kwargs['timestamp'] = time.time_ns() // 1000000
        encoded_params = urlencode(kwargs)
        signature = hmac.new(str.encode(self.__settings['secret'], encoding='utf-8'), str.encode(encoded_params, encoding='utf-8'), hashlib.sha256).hexdigest().lower()
        params = [(i, kwargs[i]) for i in kwargs.keys()]
        params.append(('signature', signature))
        headers = {
            'X-MEXC-APIKEY': self.__settings['key'],
            'Content-Type': 'application/json'
        }
        method = method.lower()
        if method == 'get':
            return requests.get(url, params=params, headers=headers)
        elif method == 'post':
            return requests.post(url, params=params, headers=headers)
        elif method == 'delete':
            return requests.delete(url, params=params, headers=headers)
        elif method == 'put':
            return requests.put(url, params=params, headers=headers)
        elif method == 'patch':
            return requests.patch(url, params=params, headers=headers)
        elif method == 'options':
            return requests.options(url, params=params, headers=headers)
        elif method == 'head':
            return requests.head(url, params=params, headers=headers)
        else:
            raise ValueError(f'Unknown method: {method}')


class Stream():
    def __init__(self, logger: Logger, settings: dict) -> None:
        super().__init__()
        self.__instance_name = None
        self.__server = None
        self.__logger = logger
        self.__settings = settings

    def on_message(self, ws, message):
        self.__logger.info(f"Received message: {message}")

    def on_error(self, ws, error):
        self.__logger.error(f"Error: {error}")

    def on_close(self, ws, close_status_code, close_msg):
        self.__logger.trace("Closed connection")

    def on_open(self, ws):
        self.__logger.trace("Connection opened")

        subscribe_request = {
            "method": "SUBSCRIPTION",
            "params": ["spot@public.deals.v3.api@BTCUSDT"],
            "id": 0
        }
        ws.send(json.dumps(subscribe_request))
        self.__logger.info(f"Sent subscribe request: {subscribe_request}")

    def subscribe_to_stream(self):
        uri = "wss://wbs.mexc.com/ws"

        ws = WebSocketApp(uri, on_message=self.on_message, on_error=self.on_error,
                          on_close=self.on_close, on_open=self.on_open)
        ws.run_forever()
