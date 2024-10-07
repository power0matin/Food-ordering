#customer validation - Aida Shams
import re

class CustomerValidation:

    @staticmethod
    def id_validator(customer_id, message):
        if type(customer_id) == int and re.match(r"^[1-9]{9}$", customer_id):
            return customer_id
        else:
            return ValueError(message)

    @staticmethod
    def name_validator(name, message):
        if type(name) == str and re.match(r"^[a-zA-Z\s]{2,20}$", name):
            return name
        else:
            raise ValueError(message)

    @staticmethod
    def email_validator(email, message):
        if re.match(r"^[a-zA-Z0-9]\w+@(gmail|yahoo).com$", email, re.I):
            return email
        else:
            raise ValueError(message)

    @staticmethod
    def phone_validator(phone, message):
        if type(phone) == str and re.match(r"^09[0-9]{9}$", phone):
            return phone
        else:
            raise ValueError(message)
