from model.entity.drink import Drink
from model.service.drink_service import DrinkService
from model.tools.decorators import exception_handling

class DrinkController:

    @classmethod
    @exception_handling
    def add_drink(cls, title, price, duration, size, status=True):
        drink = Drink(None, title, price, duration, size, status)
        DrinkService.save(drink)
        return "Drink Saved"

    @classmethod
    @exception_handling
    def update_drink(cls, drink_id, title=None, price=None, duration=None, size=None, status=None):
        drink = Drink(drink_id, title, price, duration, size, status)
        DrinkService.edit(drink)
        return "Drink Updated"

    @classmethod
    @exception_handling
    def delete_drink(cls, drink_id):
        DrinkService.remove(drink_id)
        return "Drink Deleted"

    @classmethod
    @exception_handling
    def get_drink_by_id(cls, drink_id):
        return True, DrinkService.find_by_id(drink_id)

    @classmethod
    @exception_handling
    def get_all_drinks(cls):
        return True, DrinkService.find_all()

    @classmethod
    @exception_handling
    def search_drink_by_title(cls, title):
        return True, DrinkService.find_by_title(title)

    @classmethod
    @exception_handling
    def search_drink_by_title_and_status(cls, title, status):
        return True, DrinkService.search_drink_by_title_and_status(title, status)