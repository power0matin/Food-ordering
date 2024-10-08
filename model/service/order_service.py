from model.entity.order import Order
from model.repository.crud_repository import CrudRepository


class OrderService:
    repo = CrudRepository(Order)

    @classmethod
    def save(cls, order):
        cls.repo.save(order)
        return order

    @classmethod
    def edit(cls, order):
        cls.repo.edit(order)
        return order

    @classmethod
    def remove(cls, order_id):
        cls.repo.remove(order_id)
        return order_id

    @classmethod
    def find_by_id(cls, customer_id):
        return cls.repo.find_by_id(customer_id)

    @classmethod
    def find_all(cls):
        return cls.repo.find_all()

