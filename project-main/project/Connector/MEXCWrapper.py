import websocket
import sys
import os
import requests
import logging
import logging.config
import threading
import json
import time 

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
from Declarations.IConnector import IConnector
from Declarations.models import BrokerEvent #OrderStatus, OrderType
from Declarations.models import SubscriptionModel

class MEXCWrapper(IConnector):
    def __init__(self, settings, event):
        super(IConnector, self).__init__()
        self.__settings = settings
        self.__event = event
        self.__logger = logging.getLogger('MEXC')
        self.__ws = {}
        self.__isStarted = False
        self.__connector_name = 'MEXC'
        
        
    @property
    def name(self):
        return self.__connector_name

    # @property
    # def is_connected(self):
    #     return self.__user_chnl.isConnected

    @property
    def is_started(self):
        return self.__isStarted

    def __del__(self):
        self.stop()
        
    def start(self):
        if self.__isStarted:
            self.__event(self.__connector_name, BrokerEvent.InternalError, "Connector already started")
            self.__logger.info('Cant start {}, connector already started.'.format(self.__connector_name))
            return

        
        self.__isStarted = True
        self.__event(self.__connector_name, BrokerEvent.ConnectorStarted)
        # self.__ws = SocketObj(self.name, self.__settings['wss'], self.__logger, self.__callback_sream_data, self.__event)
        # self.__ws.start()

        
    def stop(self):
        if self.__isStarted:
            self.__isStarted = False
            #self.__channels.clear()
            self.__event(self.__connector_name, BrokerEvent.ConnectorStopped)
            self.__user_chnl.stop()
        else:
            self.__event(self.__connector_name, BrokerEvent.InternalError, "Connector is not started")
            self.__logger.info('Cant stop {}, connector is not started.'.format(self.__connector_name))
            
    def subscribe(self, subscriber, symbol, model, func):
        if not self.__isStarted:
            self.__logger.info(
                'Cant subscribe {} for {}. Connector already stopped'.format(symbol['symbol']['symbol'], subscriber))
            self.__event(self.__connector_name, BrokerEvent.CoinSubscribedFault, symbol['symbol']['symbol'])
            return
        product = symbol['symbol']['symbol'].upper()
        if model == SubscriptionModel.TopBook:
        #     self.__ws.subscribe(symbol['symbol']['symbol'], 'bookTicker')
            key = '{}_{}'.format(product, 'top')
            if key in self.__ws.keys():
                return
                
            self.__ws[key] = SocketObj(self.name, self.__settings['wss'], self.__logger, func, self.__event)
            self.__ws[key].start()
            time.sleep(1)
            self.__ws[key].subscribe(product, 'bookTicker')
            
    def unsubscribe(self, subscriber, symbol, model):
        pass
        del self.__ws[key]
        
        
        
class SocketObj(object):
    def __init__(self, instance_name, url, logger, callback, event):
        self.__instance_name = instance_name
        self.__url = url
        self.__callback = callback
        self.__on_event = event
        self.__logger = logger
    
    
    def on__message(self, ws, message):
        if 'code' in message:
            return
        if 'bookTicker' in message:
            self.topParse(message)

    def on__error(self, ws, error):
        self.__logger.info('<-- Error {}--{}'.format(self.__instance_name, error))
        self.__on_event(self.__instance_name, BrokerEvent.SessionError, error)

    def on__open(self, ws):
        self.__isConnected = True
        self.__on_event(self.__instance_name, BrokerEvent.SessionLogon)
        self.__logger.info('<-- {} connection open'.format(self.__instance_name))

    def on__close(self, ws, close_status_code, close_msg):
        self.__isConnected = False
        #self.__channels.clear()
        self.__on_event(self.__instance_name, BrokerEvent.SessionLogout)
        self.__logger.info('<-- {} connection close'.format(self.__instance_name))
        
    def start(self):
        self.__ws = websocket.WebSocketApp(self.__url, 
                                           on_open=self.on__open,
                                           on_message=self.on__message,
                                           on_error=self.on__error,
                                           on_close=self.on__close)
        wst = threading.Thread(target=self.__ws.run_forever)
        wst.daemon = True
        wst.start()
        self.__isStarted = True

        self.__logger.debug('{} connection started'.format(self.__instance_name))
        
    def stop(self):
        self.__ws.close()
        # self.topBook.clear()
        # self.orderBook.clear()
        self.__logger.debug('{} stopped'.format(self.__instance_name))
    
    def isStarted(self):
        return self.__isStarted
    
    def topParse(self, message):
        msg = json.loads(message)
        md = msg['d']
        data = {}
        data['bid'] = float(md['b'])
        data['ask'] = float(md['a'])
        data['bidSize'] = float(md['B'])
        data['askSize'] = float(md['A'])
        data['symbol'] = msg['s']
        data['ts'] = msg['t']
        
        self.__callback(self.__instance_name, data['symbol'], data)
        
    def subscribe(self, symbol:str, type):
        self.__ws.send(json.dumps({
            "method": "SUBSCRIPTION",
            "params": [
                        f"spot@public.{type}.v3.api@{symbol.upper()}"
            ]
        }))
        
    def unsubscribe(self, symbol:str, type):
        self.__ws.send(json.dumps({
            "method": "SUBSCRIPTION",
            "params": [
                        f"spot@public.{type}.v3.api@{symbol.upper()}"
            ]
        }))
   