from model.entity.order import Order
from model.service.order_service import OrderService
from model.tools.decorators import *


class OrderController:

    @classmethod
    @exception_handling
    def save(cls, amount, discount, pure_amount):
        order = Order(None, amount, discount, pure_amount)
        OrderService.save(order)
        return True, "Order saved"

    @classmethod
    @exception_handling
    def edit(cls, id, amount, discount, pure_amount):
        order = Order(id, amount, discount, pure_amount)
        OrderService.edit(order)
        return True, "Order saved"

    @classmethod
    @exception_handling
    def remove(cls, id):
        OrderService.remove(id)
        return True, "Order removed"

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        OrderService.find_by_id(id)
        return True, "Order found"

    @classmethod
    @exception_handling
    def find_all(cls):
        return OrderService.find_all()
