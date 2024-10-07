import re


class AdminValidation:

    @staticmethod
    def id_validator(admin_id, message):
        if type(admin_id) == int and re.match(r"^[1-9]{7}$", admin_id):
            return admin_id
        else:
            return ValueError(message)

    @staticmethod
    def name_validator(name, message):
        if re.match(r"^[0-9a-zA-Z\s]{2,20}$", name):
            return name
        else:
            raise ValueError(message)

    @staticmethod
    def email_validation(email):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, email):
            return False, "Invalid email format."
        return True, "Valid email."

    @staticmethod
    def password_validator(password, message):
        if re.match(r"^[0-9a-zA-Z\s]{8,20}$", password):
            return password
        else:
            raise ValueError(message)
