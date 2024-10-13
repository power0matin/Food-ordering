from model.service.drink_service import DrinkService
from model.entity.drink import Drink


class DrinkController(Base):

    @classmethod
    def add_drink(cls, title, price, duration, size, status=True):
        try:
            drink =Drink(None, title, price, duration, size, status)
            DrinkService.save(drink)
            return True, "Drink saved successfully"
        except Exception as e:
            return False, str(e)

    @classmethod
    def update_drink(cls, drink_id, title=None, price=None, duration=None, size=None, status=None):
        try:
            drink = DrinkService.find_by_id(drink_id)
            if not drink:
                return False, "Drink not found"

            drink.title = title if title is not None else drink.title
            drink.price = price if price is not None else drink.price
            drink.duration = duration if duration is not None else drink.duration
            drink.size = size if size is not None else drink.size
            drink.status = status if status is not None else drink.status

            DrinkService.edit(drink)
            return True, "drink updated successfully"
        except Exception as e:
            return False, str(e)

    @classmethod
    def delete_drink(cls, drink_id):
        try:
            Service.remove(drink_id)
            drinkService.remove(drink_id)
            return True, "Drink deleted successfully"
        except Exception as e:
            return False, str(e)

    @classmethod
    def get_drink_by_id(cls, drink_id):
        try:
            drink = Drinkservice.find_by_id(drink_id)
            if not drink:
                return False, "Drink not found"
            return True, drink
        except Exception as e:
            return False, str(e)

    @classmethod
    def get_all_drinks(cls):
        try:
            drinks = DrinkService.find_all()
            return True, drink
        except Exception as e:
            return False, str(e)

    @classmethod
    def search_drink_by_title(cls, title):
        try:
            drinks = DrinkService.find_by_title(title)
            return True, drinks
        except Exception as e:
            return False, str(e)