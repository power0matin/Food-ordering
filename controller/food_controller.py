from model.entity import Food
from model.service import FoodService
from model.tools import exception_handling


class FoodController:

    @classmethod
    @exception_handling
    def save(cls, title, description, price, duration, size, available=True):
        food = Food(None, title, description, price, duration, size, available)
        FoodService.save(food)
        return food

    @classmethod
    @exception_handling
    def edit(cls, id, title, description, price, duration, size, available=True):
        food = Food(id, title, description, price, duration, size, available)
        FoodService.edit(food)
        return food

    @classmethod
    @exception_handling
    def remove(cls, id):
        return FoodService.remove(id)

    @classmethod
    @exception_handling
    def find_all(cls):
        return FoodService.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        return FoodService.find_by_id(id)

    @classmethod
    @exception_handling
    def find_by_title(cls, title):
        return FoodService.find_by_title(title)
