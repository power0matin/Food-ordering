import re


class OrderValidation:
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
