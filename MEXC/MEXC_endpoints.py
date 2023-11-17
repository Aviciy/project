from strenum import StrEnum


class MEXCEndpoints(StrEnum):
    """MEXC API endpoints"""

    # Base Endpoint
    BASE = 'https://api.mexc.com'

    # Public
    PING = 'https://api.mexc.com/api/v3/ping'
    SERVER_TIME = 'https://api.mexc.com/api/v3/time'
    EXCHANGE_INFO = 'https://api.mexc.com/api/v3/exchangeInfo'
    TICKER = 'https://api.mexc.com/api/v3/ticker/price'
    BOOK_TICKER = 'https://api.mexc.com/api/v3/ticker/bookTicker'
    BALANCES = 'https://api.mexc.com/api/v3/account'

    # Private
    ACCOUNT = 'https://api.mexc.com/api/v2/account'
    ORDER = 'https://api.mexc.com/api/v2/order'
    OPEN_ORDERS = 'https://api.mexc.com/api/v2/openOrders'
    ALL_ORDERS = 'https://api.mexc.com/api/v2/allOrders'
    MY_TRADES = 'https://api.mexc.com/api/v2/myTrades'
    WITHDRAW_HISTORY = 'https://api.mexc.com/api/v2/withdrawHistory'
    DEPOSIT_HISTORY = 'https://api.mexc.com/api/v2/depositHistory'
    DEPOSIT_ADDRESS = 'https://api.mexc.com/api/v2/depositAddress'
    TRADE_FEE = 'https://api.mexc.com/api/v2/tradeFee'
    ASSET_DETAIL = 'https://api.mexc.com/api/v2/assetDetail'
    DUST_LOG = 'https://api.mexc.com/api/v3/userAssetDribbletLog'
    DUST_TRANSFER = 'https://api.mexc.com/wapi/v3/assetDribblet'

    # Margin
    MARGIN_ALL_ORDERS = 'https://api.mexc.com/sapi/v1/margin/allOrders'
    MARGIN_OPEN_ORDERS = 'https://api.mexc.com/sapi/v1/margin/openOrders'
    MARGIN_ACCOUNT = 'https://api.mexc.com/sapi/v1/margin/account'
    MARGIN_ORDER = 'https://api.mexc.com/sapi/v1/margin/order'
    MARGIN_MY_TRADES = 'https://api.mexc.com/sapi/v1/margin/myTrades'
    MARGIN_MAX_BORROWABLE = 'https://api.mexc.com/sapi/v1/margin/maxBorrowable'
    MARGIN_MAX_TRANSFERABLE = 'https://api.mexc.com/sapi/v1/margin/maxTransferable'
    MARGIN_TRANSFER = 'https://api.mexc.com/sapi/v1/margin/transfer'
    MARGIN_REPAY = 'https://api.mexc.com/sapi/v1/margin/repay'
