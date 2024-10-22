from model.entity import Payment
from model.repository import CrudRepository


class PaymentService:
    repo = CrudRepository(Payment)

    @classmethod
    def save(cls, payment):
        return cls.repo.save(payment)

    @classmethod
    def edit(cls, payment):
        return cls.repo.edit(payment)

    @classmethod
    def remove(cls, id):
        return cls.repo.remove(id)

    @classmethod
    def find_all(cls):
        return cls.repo.find_all()

    @classmethod
    def find_by_id(cls, id):
        return cls.repo.find_by_id(id)

    @classmethod
    def find_by_payment_type(cls, payment_type):
        return cls.repo.find_by(Payment.payment_type == payment_type)

    @classmethod
    def find_by_amount(cls, amount):
        return cls.repo.find_by(Payment.amount == amount)

    @classmethod
    def find_by_order(cls, order):
        return cls.repo.find_by(Payment.order == order)
