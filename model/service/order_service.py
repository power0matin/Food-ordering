from model.entity import Order
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
    def remove(cls, id):
        cls.repo.remove(id)
        return id

    @classmethod
    def find_by_id(cls, id):
        return cls.repo.find_by_id(id)

    @classmethod
    def find_all(cls):
        return cls.repo.find_all()
