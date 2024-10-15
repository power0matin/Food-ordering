from model.entity.order import Order
from model.service.order_service import OrderService
from model.tools.decorators import *


class OrderController:

    @classmethod
    @exception_handling
    def save(cls, order_id, amount, discount, pure_amount):
        order = Order(order_id, amount, discount, pure_amount)
        OrderService.save(order)
        return True, "Order saved"

    @classmethod
    @exception_handling
    def edit(cls, order_id, amount, discount, pure_amount):
        order = Order(order_id, amount, discount, pure_amount)
        OrderService.edit(order)
        return True, "Order saved"

    @classmethod
    @exception_handling
    def remove(cls, order_id):
        OrderService.remove(order_id)
        return True, "Order removed"

    @classmethod
    @exception_handling
    def find_by_id(cls, order_id):
        OrderService.find_by_id(order_id)
        return True, "Order found"

    @classmethod
    @exception_handling
    def find_all(cls):
        return OrderService.find_all()
