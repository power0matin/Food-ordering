# customer service - Aida Shams
# using class method
from model.entity import Customer
from model.repository.crud_repository import CrudRepository


class CustomerService:
    repo = CrudRepository(Customer)

    # save:
    @classmethod
    def save(cls, customer):
        cls.repo.save(customer)
        return customer

    # edit:
    @classmethod
    def edit(cls, customer):
        cls.repo.edit(customer)
        return customer

    # remove:
    @classmethod
    def remove(cls, id):
        cls.repo.remove(id)
        return id

    # find all:
    @classmethod
    def find_all(cls):
        return cls.repo.find_all()

    # find by id:
    @classmethod
    def find_by_id(cls, id):
        return cls.repo.find_by_id(id)

    # find by username:
    @classmethod
    def find_by_username(cls, username):
        return cls.repo.find_by(Customer.username == username)

    # find by username AND password:
    @classmethod
    def find_by_username_and_password(cls, username, password):
        return cls.repo.find_by(Customer.password == password and Customer.username == username)
