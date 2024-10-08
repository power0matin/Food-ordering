import re


class Validation:
    @staticmethod
    def id_validator(admin_id, message):
        if type(admin_id) == int and re.match(r"^[1-9][0-9]{0,6}$", str(admin_id)):
            return admin_id
        else:
            return ValueError(message)

    @staticmethod
    def name_validator(name, message):
        if type(name) == str and re.match(r"^[a-zA-Z\s]{2,20}$", name):
            return name
        else:
            return ValueError(message)

    @staticmethod
    def family_validator(family, message):
        if type(family) == str and re.match(r"^[a-zA-Z\s]{2,20}$", family):
            return family
        else:
            return ValueError(message)

    @staticmethod
    def username_validator(username, message):
        if type(username) == str and re.match(r"^[a-zA-Z0-9]{5,}$", username):
            return username
        else:
            return ValueError(message)

    @staticmethod
    def password_validator(password, message):
        if type(password) == str and re.match(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", password):
            return password
        else:
            return ValueError(message)

    @staticmethod
    def access_level_validator(access_level, message):
        if type(access_level) == int and 0 <= access_level <= 10:
            return access_level
        else:
            return ValueError(message)
