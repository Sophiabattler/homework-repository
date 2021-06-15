"""Task02 - Strategies"""
from typing import Callable, Union


def morning_discount(order: "Order") -> float:
    return order.price * 0.5


def elder_discount(order: "Order") -> float:
    return order.price * 0.9


class Order:
    def __init__(
        self, price: Union[int, float], discount: Callable[["Order"], Union[int, float]]
    ):
        self.price = price
        self.discount = discount

    def final_price(self) -> Union[int, float]:
        return self.price - self.discount(self)
