from model.entity import Customer, and_
from model.repository import CrudRepository


class CustomerService:
    repo = CrudRepository(Customer)

    @classmethod
    def save(cls, customer):
        return cls.repo.save(customer)

    @classmethod
    def edit(cls, customer):
        return cls.repo.edit(customer)

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
    def find_by_username(cls, username):
        return cls.repo.find_by(Customer.username == username)

    @classmethod
    def find_by_username_and_password(cls, username, password):
        return cls.repo.find_by(and_(Customer.password == password, Customer.username == username))
