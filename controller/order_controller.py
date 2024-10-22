from model.entity import Order
from model.service import OrderService
from model.tools import *


class OrderController:

    @classmethod
    @exception_handling
    def save(cls, amount, discount, pure_amount):
        order = Order(None, amount, discount, pure_amount)
        OrderService.save(order)
        return order

    @classmethod
    @exception_handling
    def edit(cls, id, amount, discount, pure_amount):
        order = Order(id, amount, discount, pure_amount)
        OrderService.edit(order)
        return order

    @classmethod
    @exception_handling
    def remove(cls, id):
        return OrderService.remove(id)

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        return OrderService.find_by_id(id)

    @classmethod
    @exception_handling
    def find_all(cls):
        return OrderService.find_all()
