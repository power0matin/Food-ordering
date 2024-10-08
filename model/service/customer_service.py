#customer service - Aida Shams

from model.entity.customer import Customer
from model.repository.crud_repository import CrudRepository


class CustomerService:
    repo = CrudRepository(Customer)

    @classmethod
    def save(cls, customer):
        cls.repo.save(customer)
        return customer

    @classmethod
    def edit(cls, customer):
        cls.repo.edit(customer)
        return customer

    @classmethod
    def remove(cls, customer_id):
        cls.repo.remove(customer_id)
        return customer_id

    @classmethod
    def find_all(cls):
        return cls.repo.find_all()

    @classmethod
    def find_by_id(cls, customer_id):
        return cls.repo.find_by_id(customer_id)

    @classmethod
    def find_by_username(cls, username):
        return cls.repo.find_by_username(username)

    @classmethod
    def find_by_username_and_password(cls, username, password):
        return cls.repo.find_by_username_and_password(username, password)