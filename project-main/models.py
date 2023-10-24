class BrokerEvent:
    SessionLogon = "SessionLogon"
    SessionLogout = "SessionLogout"
    SessionError = "SessionError"
    InternalError = "InternalError"
    WarningDelay = "WarningDelay"
    MaximumDelay = "MaximumDelay"
    ConnectorStarted = "ConnectorStarted"
    ConnectorStopped = "ConnectorStopped"
    CoinSubscribed = "CoinSubscribed"
    CoinUnsubscribed = "CoinUnsubscribed"
    CoinSubscribedFault = "CoinSubscribedFault"
    CoinUnsubscribedFault = "CoinUnsubscribedFault"

class SubscriptionModel:
    TopBook = "TopBook"
    FullBook = "FullBook"
    Trade = "Trade"

class OrderType:
    Market = 'Market'
    Limit = 'Limit'

class OrderStatus:
    PartiallyFilled = 'PartiallyFilled'
    Filled = 'Filled'
    New = 'New'
    Canceled = 'Canceled'
    Replaced = 'Replaced'
    Rejected = 'Rejected'
    CancelRejected = 'CancelRejected'

class TimeInForce:
    Day = 'Day'
    GoodTillCancel = 'GoodTillCancel'
    ImmediateOrCancel = 'ImmediateOrCancel'
    FillOrKill = 'FillOrKill'
