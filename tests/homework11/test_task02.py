"""Test for task02 - Strategies"""
from homework11.task02 import Order, elder_discount, morning_discount


def test_order_with_different_discounts():
    order_1 = Order(100, morning_discount)
    assert order_1.final_price() == 50
    order_2 = Order(100, elder_discount)
    assert order_2.final_price() == 10
