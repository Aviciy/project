import hashlib
import hmac
import time
from urllib.parse import urlencode

import requests

from Abstract.connector import Connector
from Abstract.logger import Logger
from MEXC import Endpoints


# def subscribe() -> None:
#     subscription = {
#         "method": "SUBSCRIPTION",
#         "params": ["spot@public.deals.v3.api@BTCUSDT"]
#     }
# 
#     json.dumps(subscription)
# 
# 
# def unsubscr7ibe() -> None:
#     unsubscription = {
#         "method": "UNSUBSCRIPTION",
#         "params": ["spot@public.deals.v3.api@BTCUSDT", "spot@public.increase.depth.v3.api@BTCUSDT"]
#     }
# 
#     json.dumps(unsubscription)


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
            # return requests.get(self.__make_endpoint(MEXCEndpoints.PING)).json()['PING'].ok
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
            self.__loger.error(f'Error getting server time: {e}')
            return None

    def get_ticker(self, symbol: str) -> float | None:
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

    def get_balances(self) -> dict | None:
        try:
            self.__logger.trace('Return balance data')
            response = self.__make_signed_request(Endpoints.BALANCES, 'get').json()
            print(response)
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

    def get_timestamp(self) -> str:
        return int(round(time.time() * 1000))

    def balances(self) -> dict:
        balances = {}
        key = 'mx0vglWmEenQD2ddFS'

        params = {"timestamp": self.get_timestamp()}
        headers = {
            'X-MEXC-APIKEY': key,
            'Content-Type': 'application/json'
        }
        query = urlencode(params)
        params["signature"] = hmac.new(query.encode("utf8"),
                                       digestmod=hashlib.sha256).hexdigest()
        url = Endpoints.BASE + "/api/v3/account" + "?" + urlencode(params)
        res = requests.get(url, headers=headers).json()
        return res
    # def start(self) -> bool:
    #     if not self.check_connection():
    #         self.__logger.error('Connection to MEXC failed.')
    #         return False
    #     self.__logger.info('MEXC-Connector started')
    #     return True
    #
    # def on_event(self, broker_event: object, details: object) -> None:
    #     print('--- {}-{}-{}'.
    #           format(self,
    #                  broker_event,
    #                  details
    #                  )
    #           )
    #
    # def top_parse(self, message: str) -> None:
    #     msg = json.loads(message)
    #     md = msg['d']
    #     data = {'bid': float(md['b']), 'ask': float(md['a']), 'bidSize': float(md['B']), 'askSize': float(md['A']), 'symbol': msg['s'], 'ts': msg['t']}
    #
    #     self.__callback(self.__instance_name, data['symbol'], data)
    #
    # def __callback(self, __instance_name, param, data):
    #     pass
