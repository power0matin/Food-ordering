# costumer controller - Aida Shams
# using class method

from model.entity.customer import Customer
from model.service.customer_service import CustomerService
from model.tools.decorators import exception_handling


class CustomerController:

    # save:
    @classmethod
    @exception_handling
    def save(cls, name, family, email, phone, username, password):
        customer = Customer(None, name, family, email, phone, username, password)
        CustomerService.save(customer)
        return customer

    # edit:
    @classmethod
    @exception_handling
    def edit(cls, id, name, family, email, phone, username, password):
        customer = Customer(id, name, family, email, phone, username, password)
        CustomerService.edit(customer)
        return customer

    # remove:
    @classmethod
    @exception_handling
    def remove(cls, id):
        old_customer = CustomerService.remove(id)
        return old_customer

    # find all:
    @classmethod
    @exception_handling
    def find_all(cls):
        return True, CustomerService.find_all()

    # find by id:
    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        return True, CustomerService.find_by_id(id)

    # find by username:
    @classmethod
    @exception_handling
    def find_by_username(cls, username):
        return True, CustomerService.find_by_username(username)

    # find by username AND password:
    @classmethod
    @exception_handling
    def find_by_username_and_password(cls, username, password):
        return True, CustomerService.find_by_username_and_password(username, password)

# CustomerController.save("ali", "alipour", "ali","a123")
