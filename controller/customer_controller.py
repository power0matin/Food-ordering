#costumer controller - Aida Shams
#same error from external libraries!!!

from model.entity.customer import Customer
from model.service.customer_service import CustomerService

class CustomerController:

    @classmethod
    def save(cls, name, email, phone):
        try:
            customer = Customer(None, name, email, phone)
            CustomerService.save(customer)
            return True, "Customer Saved!"
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, customer_id, name, email, phone):
        try:
            customer = Customer(customer_id, name, email, phone)
            CustomerService.edit(customer)
            return True, "Customer Edited!"
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, customer_id):
        try:
            CustomerService.remove(customer_id)
            return True, "Customer Removed!"
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            return True, CustomerService.find_all()
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_id(cls, customer_id):
        try:
            return True, CustomerService.find_by_id(customer_id)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by(cls, by):
        try:
            return True, CustomerService.find_by(by)
        except Exception as e:
            return False, str(e)