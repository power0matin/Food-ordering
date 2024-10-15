from model.entity.payment import Payment
from model.service.payment_service import PaymentService
from model.tools.decorators import exception_handling

class CustomerController:

    @classmethod
    @exception_handling
    def save(cls, amount, payment_type, description, order):
        payment = Payment(None, amount, payment_type, description, order)
        PaymentService.save(payment)
        return True, "Payment Saved!"

    @classmethod
    @exception_handling
    def edit(cls, id, amount, payment_type, description, order):
        payment = Payment(id, amount, payment_type, description, order)
        PaymentService.edit(payment)
        return True, "Payment Edited!"

    @classmethod
    @exception_handling
    def remove(cls, id):
        PaymentService.remove(id)
        return True, "Payment Removed!"

    @classmethod
    @exception_handling
    def find_all(cls):
        return True, PaymentService.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        return True, PaymentService.find_by_id(id)