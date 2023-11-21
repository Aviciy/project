import hashlib
import hmac
import json
import threading
import time
from urllib.parse import urlencode

import requests
from requests import Response
from self import self
from websocket._app import WebSocketApp

from Abstract.connector import Connector
from Abstract.logger import Logger
from Abstract.websocket_handler import WebSocketHandler
from MEXC import Endpoints


class MEXCConnector(Connector):

    def __init__(self, logger: Logger, websocket_handler: WebSocketHandler, settings: dict) -> None:
        super().__init__()
        self.__instance_name = None
        self.__server = None
        self.__logger = logger
        self.__settings = settings
        self.__websocket = None
        self.__websocket_thread = None
        self.__is_started = False
        self.__nonce = 0
        self.__websocket_handler = websocket_handler
        self.__logger.trace('MEXCConnector was created')

    def start(self) -> bool:
        if self.__websocket is not None:
            self.__logger.warning('MEXCConnector is already started')
            return True
        try:
            self.__websocket = WebSocketApp(Endpoints.WEBSOCKET_BASE,
                                            on_message=self.__websocket_handler.on_message,
                                            on_error=self.__websocket_handler.on_error,
                                            on_close=self.__websocket_handler.on_close,
                                            on_open=self.__websocket_handler.on_open)
            self.__websocket_thread = threading.Thread(target=self.__websocket.run_forever)
            self.__websocket_thread.start()
            self.__is_started = True
        except Exception as e:
            self.__logger.error(f'Error starting MEXCConnector: {e}')
            return False
        return True

    def stop(self) -> bool:
        if not self.__is_started:
            self.__logger.warning('MEXCConnector is already stopped')
            return True
        try:
            self.__websocket.close()
            self.__websocket_thread.join()
            self.__is_started = False
        except Exception as e:
            self.__logger.error(f'Error stopping MEXCConnector: {e}')
            return False
        return True

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

    def get_ticker(self, symbol: 'BTCUSDT') -> dict | None:
        try:

            self.__logger.trace('Return ticker')

            url = f"{Endpoints.TICKER}?symbol={symbol}"
            response = requests.get(url).json()
            price = response['price']
            result = (f"{symbol} -> {price}")
            self.__logger.debug(result)
            return result
        except Exception as e:
            self.__logger.error(f'Error getting ticker: {e}')
            return None

    def get_exchange_info(self) -> [str] or None:
        self.__logger.trace('Return exchange info')
        try:
            response = requests.get(Endpoints.EXCHANGE_INFO).json()
            symbols = [item['symbol'] for item in response.get('symbols', [])]
            result = ', '.join(symbols[:5])
            if len(symbols) > 5:
                result += "..."
            self.__logger.debug(result)
            return result
        except Exception as e:
            self.__logger.error(f'Error getting exchange info: {e}')
            return None

    def get_balances(self) -> object | None:
        try:
            self.__logger.trace('Return balance data')
            response = self.__make_signed_request(Endpoints.BALANCES, 'get').json()
            return response
        except Exception as e:
            self.__logger.error(f'Error getting balance info: {e}')
            return None

    def get_book(self, symbol: 'BTCUSDT') -> dict | None:
        try:
            self.__logger.trace('Return book')
            url = f"{Endpoints.BOOK_TICKER}?symbol={symbol}"
            response = requests.get(url).json()
            formatted_data = {
                'bids': [{'price': float(response['bidPrice']), 'quantity': float(response['bidQty'])}],
                'asks': [{'price': float(response['askPrice']), 'quantity': float(response['askQty'])}]
            }

            result = (f"{symbol} -> {formatted_data}")
            self.__logger.debug(result)
            return response
        except Exception as e:
            self.__logger.error(f'Error getting book: {e}')
            return None

    def subscribe(self, symbol: str) -> bool:
        subscribe_request = {
            "method": "SUBSCRIPTION",
            "params": [f"spot@public.deals.v3.api@{symbol}"],
            "id": str(self.__get_nonce())
        }
        self.__websocket.send(json.dumps(subscribe_request))
        self.__logger.info(f'Send subscribe request: {subscribe_request}')
        return True

    def unsubscribe(self, symbol: str) -> bool:
        unsubscribe_request = {
            "method": "UNSUBSCRIPTION",
            "params": [f"spot@public.deals.v3.api@{symbol}"],
            "id": str(self.__get_nonce())
        }
        self.__websocket.send(json.dumps(unsubscribe_request))
        self.__logger.info(f'Send unsubscribe request: {unsubscribe_request}')
        return True

    def __get_nonce(self) -> int:
        nonce = self.__nonce
        self.__nonce += 1
        return self.__nonce

    def __make_signed_request(self, url: str, method: str, **kwargs) -> Response:
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
