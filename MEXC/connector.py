import logging
import logging.config

from Shared.connector import Connector


class MEXCConnector(Connector):
    def __init__(self, settings):
        super().__init__()
        self.__settings = settings
        self.__connector_name = 'MEXC'

    def get_name(self):
        raise NotImplementedError

    def check_connection(self):
        raise NotImplementedError

    def get_server_time(self):
        raise NotImplementedError

    def get_exchange_info(self):
        raise NotImplementedError

    def get_ticker(self, symbol):
        raise NotImplementedError

    def get_book(self, symbol):
        raise NotImplementedError

    def get_balances(self):
        raise NotImplementedError
