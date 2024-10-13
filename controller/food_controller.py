from model.service.food_service import FoodService
from model.entity.food import Food


class FoodController:

    @classmethod
    def add_food(cls, title, price, duration, description, size, status=True):
        try:
            food = Food(None, title, price, duration, description, size, status)
            FoodService.save(food)
            return True, "Food saved successfully"
        except Exception as e:
            return False, str(e)

    @classmethod
    def update_food(cls, food_id, title=None, price=None, duration=None, description=None, size=None, status=None):
        try:
            food = FoodService.find_by_id(food_id)
            if not food:
                return False, "Food not found"

            food.title = title if title is not None else food.title
            food.price = price if price is not None else food.price
            food.duration = duration if duration is not None else food.duration
            food.description = description if description is not None else food.description
            food.size = size if size is not None else food.size
            food.status = status if status is not None else food.status

            FoodService.edit(food)
            return True, "Food updated successfully"
        except Exception as e:
            return False, str(e)

    @classmethod
    def delete_food(cls, food_id):
        try:
            FoodService.remove(food_id)
            return True, "Food deleted successfully"
        except Exception as e:
            return False, str(e)

    @classmethod
    def get_food_by_id(cls, food_id):
        try:
            food = FoodService.find_by_id(food_id)
            if not food:
                return False, "Food not found"
            return True, food
        except Exception as e:
            return False, str(e)

    @classmethod
    def get_all_foods(cls):
        try:
            foods = FoodService.find_all()
            return True, foods
        except Exception as e:
            return False, str(e)

    @classmethod
    def search_food_by_title(cls, title):
        try:
            foods = FoodService.find_by_title(title)
            return True, foods
        except Exception as e:
            return False, str(e)
