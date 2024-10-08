import re

class Validation:

    @staticmethod
    def id_validator(id,message):
        if type(id) == int and re.match(r"^[1-9]{7}$", id):
            return id
        else:
            return ValueError(message)


    @staticmethod
    def title_validator(title,message):
        if type(title) == str and re.match(r"^[A-Za-z\s]$", title):
            return title
        else:
            return ValueError(message)

    @staticmethod
    def location_validator(location,message):
        if type(location) == str and re.match(r"^[A-Za-z\s0-9]$", location):
            return location
        else:
            return ValueError(message)

    @staticmethod
    def number_validator(number,message):
        if type(number) == int and re.match(r"^[1-9]{2}$", number):
            return number
        else:
            return ValueError(message)

    @staticmethod
    def is_empty_validator(is_empty,message):
        if type(is_empty) == bool:
            return is_empty
        else:
            return ValueError(message)




