#costumer controller - Aida Shams
#using class method
#can't run : same error from external libraries!!!

from model.entity.customer import Customer
from model.service.customer_service import CustomerService

class CustomerController:

    @classmethod
    def save(cls, name, family, email, phone, username, password):
        try:
            customer = Customer(None, name, family, email, phone, username, password)
            CustomerService.save(customer)
            return True, "Customer Saved!"
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, id, name, family, email, phone, username, password):
        try:
            customer = Customer(id, name, family, email, phone, username, password)
            CustomerService.edit(customer)
            return True, "Customer Edited!"
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, id):
        try:
            CustomerService.remove(id)
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
    def find_by_id(cls, id):
        try:
            return True, CustomerService.find_by_id(id)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_username(cls, username):
        try:
            return True, CustomerService.find_by_username(username)
        except Exception as e:
            return False, str(e)
#note to me: check the following def
    @classmethod
    def find_by_username_and_password(cls, username, password):
        try:
            return True, CustomerService.find_by_username_and_password(username, password)
        except Exception as e:
            return False, str(e)


#CustomerController.save("ali", "alipour", "ali","a123")