from model.entity import Payment
from model.service import PaymentService
from model.tools import exception_handling


class PaymentController:

    @classmethod
    @exception_handling
    def save(cls, amount, payment_type, description, order):
        payment = Payment(None, amount, payment_type, description, order)
        PaymentService.save(payment)
        return payment

    @classmethod
    @exception_handling
    def edit(cls, id, amount, payment_type, description, order):
        payment = Payment(id, amount, payment_type, description, order)
        PaymentService.edit(payment)
        return payment

    @classmethod
    @exception_handling
    def remove(cls, id):
        return PaymentService.remove(id)

    @classmethod
    @exception_handling
    def find_all(cls):
        return  PaymentService.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        return  PaymentService.find_by_id(id)

    @classmethod
    @exception_handling
    def find_by_payment_type(cls, payment_type):
        return  PaymentService.find_by_payment_type(payment_type)

    @classmethod
    @exception_handling
    def find_by_amount(cls, amount):
        return  PaymentService.find_by_amount(amount)

    @classmethod
    @exception_handling
    def find_by_order(cls, order):
        return  PaymentService.find_by_order(order)
