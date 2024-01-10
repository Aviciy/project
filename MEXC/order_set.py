class Order:
    def __init__(self, order_id=None, order_state="undefined", price=None, volume=None, date_created=None, status=None):
        self.order_id = order_id
        self.order_state = order_state
        self.price = price
        self.volume = volume
        self.type = type
        self.status = status
        self.order_id = order_id
        self.date_created = date_created


def order_set(order: Order) -> Order | None:
    if order.order_state == "undefined":
        raise ValueError("Order must be in created state to be placed")
    elif order.order_state == "created":
        pass
    elif order.order_state == "placed":
        pass
    elif order.order_state == "rejected":
        pass
    elif order.order_state == "filled":
        pass
    elif order.order_state == "cancelled":
        pass
