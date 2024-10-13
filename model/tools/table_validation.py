import re

class TableValidation:

    @staticmethod
    def id_validator(id,message):
        if type(id) == int and id >= 0:
            return id
        else:
            raise ValueError(message)


    @staticmethod
    def title_validator(title,message):
        if type(title) == str and re.match(r"^[A-Za-z\s]$", title):
            return title
        else:
            raise ValueError(message)

    @staticmethod
    def location_validator(location,message):
        if type(location) == str and re.match(r"^[A-Za-z\s0-9]$", location):
            return location
        else:
            raise ValueError(message)

    @staticmethod
    def number_validator(number,message):
        if type(number) == int and number >= 0:
            return number
        else:
            raise ValueError(message)

    @staticmethod
    def is_empty_validator(is_empty,message):
        if type(is_empty) == bool and is_empty == True:
            return is_empty
        else:
            raise ValueError(message)




