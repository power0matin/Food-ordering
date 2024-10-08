class FoodValidation:
    @staticmethod
    def name_validator(name, error_message):
        if not name or len(name) > 50:
            raise ValueError(error_message)
        return name

    @staticmethod
    def description_validator(description, error_message):
        if not description or len(description) > 100:
            raise ValueError(error_message)
        return description

    @staticmethod
    def price_validator(price, error_message):
        if price <= 0:
            raise ValueError(error_message)
        return price
