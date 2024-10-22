from model.entity import Customer
from model.service import CustomerService
from model.tools import exception_handling


class CustomerController:

    @classmethod
    @exception_handling
    def save(cls, name, family, email, phone, username, password):
        customer = Customer(None, name, family, email, phone, username, password)
        CustomerService.save(customer)
        return customer

    @classmethod
    @exception_handling
    def edit(cls, id, name, family, email, phone, username, password):
        customer = Customer(id, name, family, email, phone, username, password)
        CustomerService.edit(customer)
        return customer

    @classmethod
    @exception_handling
    def remove(cls, id):
        return CustomerService.remove(id)

    @classmethod
    @exception_handling
    def find_all(cls):
        return  CustomerService.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        return  CustomerService.find_by_id(id)

    @classmethod
    @exception_handling
    def find_by_username(cls, username):
        return  CustomerService.find_by_username(username)

    @classmethod
    @exception_handling
    def find_by_username_and_password(cls, username, password):
        return  CustomerService.find_by_username_and_password(username, password)
