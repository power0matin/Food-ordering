#customer validation - Aida Shams
import re

class CustomerValidation:

    @staticmethod
    def id_validator(id, message):
        if type(id) == int and re.match(r"^[1-9][0-9]{0,6}$", id):
            return id
        else:
            return ValueError(message)

    @staticmethod
    def name_validator(name, message):
        if type(name) == str and re.match(r"^[a-zA-Z\s]{2,20}$", name):
            return name
        else:
            raise ValueError(message)

    @staticmethod
    def family_validator(family, message):
        if type(family) == str and re.match(r"^[a-zA-Z\s]{2,20}$", family):
            return family
        else:
            raise ValueError(message)

    @staticmethod
    def username_validator(username, message):
        if type(username) == str and re.match(r"^[a-zA-Z0-9\s]{2,20}$", username):
            return username
        else:
            raise ValueError(message)

    @staticmethod
    def password_validator(password, message):
        if type(password) == str and re.match(r"^[a-zA-Z0-9]{8,}$", password):
            return password
        else:
            raise ValueError(message)