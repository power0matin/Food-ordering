from model.entity import Drink
from model.service import DrinkService
from model.tools import exception_handling


class DrinkController:

    @classmethod
    @exception_handling
    def save(cls, title, price, duration, size, available=True):
        drink = Drink(None, title, price, duration, size, available)
        DrinkService.save(drink)
        return drink

    @classmethod
    @exception_handling
    def edit(cls, id, title, price, duration, size, available=True):
        drink = Drink(id, title, price, duration, size, available)
        DrinkService.edit(drink)
        return drink


    @classmethod
    @exception_handling
    def remove(cls, id):
        return  DrinkService.remove(id)


    @classmethod
    @exception_handling
    def find_all(cls):
        return DrinkService.find_all()


    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        return DrinkService.find_by_id(id)


    @classmethod
    @exception_handling
    def find_by_title(cls, title):
        return DrinkService.find_by_title(title)
