from model.entity.food import Food
from model.service.food_service import FoodService
from model.tools.decorators import exception_handling


class FoodController:

    @classmethod
    @exception_handling
    def add_food(cls, title, price, duration, description, size, status=True):
        food = Food(None, title, price, duration, description, size, status)
        FoodService.save(food)
        return "Food Saved"

    @classmethod
    @exception_handling
    def update_food(cls, food_id, title=None, price=None, duration=None, description=None, size=None, status=None):
        food = Food(food_id, title, price, duration, description, size, status)
        FoodService.edit(food)
        return "Food Updated"

    @classmethod
    @exception_handling
    def delete_food(cls, food_id):
        FoodService.remove(food_id)
        return "Food Deleted"

    @classmethod
    @exception_handling
    def get_food_by_id(cls, food_id):
        return True, FoodService.find_by_id(food_id)

    @classmethod
    @exception_handling
    def get_all_foods(cls):
        return True, FoodService.find_all()

    @classmethod
    @exception_handling
    def search_food_by_title(cls, title):
        return True, FoodService.find_by_title(title)
