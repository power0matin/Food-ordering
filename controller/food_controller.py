from model.entity.food import Food
from model.service.food_service import FoodService
from model.tools.decorators import exception_handling


class FoodController:

    # save:
    @classmethod
    @exception_handling
    def save(cls, title, description, price, duration, size, available=True):
        food = Food(None, title, description, price, duration, size, available)
        FoodService.save(food)
        return True, "Food Saved!"

    # edit:
    @classmethod
    @exception_handling
    def edit(cls, id, title, description, price, duration, size, available=True):
        food = Food(id, title, description, price, duration, size, available)
        FoodService.edit(food)
        return True, "Food Edited!"

    # remove:
    @classmethod
    @exception_handling
    def remove(cls, id):
        FoodService.remove(id)
        return True, "Food Removed!"

    # find all:
    @classmethod
    @exception_handling
    def find_all(cls):
        return True, FoodService.find_all()

    # find by id:
    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        return True, FoodService.find_by_id(id)

    # find by title:
    @classmethod
    @exception_handling
    def find_by_title(cls, title):
        return True, FoodService.find_by_title(title)
