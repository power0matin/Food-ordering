class FoodValidation:
    @staticmethod
    def title_validator(title, error_message):
        if not title or len(title) > 50:
            raise ValueError(error_message)
        return title

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

    @staticmethod
    def duration_validator(duration, error_message):
        if duration <= 0:
            raise ValueError(error_message)
        return duration

    @staticmethod
    def size_validator(size, error_message):
        if not size or len(size) > 10:
            raise ValueError(error_message)
        return size
