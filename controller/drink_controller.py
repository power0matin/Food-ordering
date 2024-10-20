from model.entity.drink import Drink
from model.service.drink_service import DrinkService
from model.tools.decorators import exception_handling


class DrinkController:


    @classmethod
    @exception_handling
    def save(cls, title, price, duration, size, available=True):
        drink = Drink(None, title, price, duration, size, available)
        DrinkService.save(drink)
        return True, "Drink Saved!"

    @classmethod
    @exception_handling
    def edit(cls, id, title, price, duration, size, available=True):
        drink = Drink(id, title, price, duration, size, available)
        DrinkService.edit(drink)
        return True, "Drink Edited!"


    @classmethod
    @exception_handling
    def remove(cls, id):
        DrinkService.remove(id)
        return True, "Drink Removed!"


    @classmethod
    @exception_handling
    def find_all(cls):
        return True, DrinkService.find_all()


    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        return True, DrinkService.find_by_id(id)


    @classmethod
    @exception_handling
    def find_by_title(cls, title):
        return True, DrinkService.find_by_title(title)
