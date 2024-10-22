import re


def pattern_validator(pattern, message):
    def inner(function_name):
        def inner2(self, value):
            if type(value) == str and re.match(pattern, value):
                function_name(self, value)
            else:
                raise ValueError(message)
        return inner2
    return inner


class Validation:
    @staticmethod
    def pattern_validator(variable, pattern, message):
        if type(variable) == str and re.match(pattern, variable):
            return variable
        else:
            raise ValueError(message)

    @staticmethod
    def id_validator(id, message):
        if isinstance(id, int) and id > 0:
            return id
        else:
            ValueError(message)

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
        if type(access_level) == int and 0 <= access_level <= 10000:
            return access_level
        else:
            return ValueError(message)

    @staticmethod
    def email_validator(email, message):
        if re.match(r"^[a-zA-Z0-9]\w+@(gmail|yahoo).com$", email):
            return email
        else:
            return ValueError(message)

    @staticmethod
    def phone_validator(phone, message):
        if type(phone) == str and re.match(r"^09[0-9]{9}$", phone):
            return phone
        else:
            return ValueError(message)

    @staticmethod
    def title_validator(title, error_message):
        if title or len(title) > 50:
            return title
        else:
            raise ValueError(error_message)

    @staticmethod
    def price_validator(price, error_message):
        if price <= 0:
            raise ValueError(error_message)
        return price

    @staticmethod
    def duration_validator(duration, error_message):
        if duration <= 0:
            raise ValueError(error_message)
        return duration

    @staticmethod
    def size_validator(size, error_message):
        if type(size) == str and re.match(r"^[a-zA-Z0-9\s]{3,25}$", size):
            return size
        else:
            raise ValueError(error_message)


    @staticmethod
    def description_validator(description, error_message):
        if not description or len(description) > 100:
            raise ValueError(error_message)
        return description

    @staticmethod
    def is_empty_validator(is_empty, message):
        if type(is_empty) == bool:
            return is_empty
        else:
            raise ValueError(message)


    @staticmethod
    def number_validator(number, message):
        if type(number) == int and number >= 0:
            return number
        else:
            raise ValueError(message)

    @staticmethod
    def amount_validator(amount, message):
        if amount <= 0:
            raise ValueError(message)
        return amount

    @staticmethod
    def discount_validator(discount, message):
        if discount == 0:
            raise ValueError(message)
        else:
            return discount

    @staticmethod
    def pure_amount_validator(pure_amount, message):
        if pure_amount <= 0:
            raise ValueError(message)
        else:
            return pure_amount

    @staticmethod
    def payment_type_validator(payment_type, message):
        if type(payment_type) == str and re.match(r"^(Online|In Person)$", payment_type):
            return payment_type
        else:
            return ValueError(message)