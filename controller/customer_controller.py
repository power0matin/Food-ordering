#costumer controller - Aida Shams
#using class method
#can't run : same error from external libraries!!!

from model.entity.customer import Customer
from model.service.customer_service import CustomerService
from model.tools.decorators import exception_handling


class CustomerController:

    @classmethod
    @exception_handling
    def save(cls, name, family, email, phone, username, password):
        customer = Customer(None, name, family, email, phone, username, password)
        CustomerService.save(customer)
        return True, "Customer Saved!"

    @classmethod
    @exception_handling
    def edit(cls, id, name, family, email, phone, username, password):
        customer = Customer(id, name, family, email, phone, username, password)
        CustomerService.edit(customer)
        return True, "Customer Edited!"

    @classmethod
    @exception_handling
    def remove(cls, id):
        CustomerService.remove(id)
        return True, "Customer Removed!"

    @classmethod
    @exception_handling
    def find_all(cls):
        return True, CustomerService.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        return True, CustomerService.find_by_id(id)

    @classmethod
    @exception_handling
    def find_by_username(cls, username):
        return True, CustomerService.find_by_username(username)

#note to me: check the following def
    @classmethod
    @exception_handling
    def find_by_username_and_password(cls, username, password):
        return True, CustomerService.find_by_username_and_password(username, password)

#CustomerController.save("ali", "alipour", "ali","a123")