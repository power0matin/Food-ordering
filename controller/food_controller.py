from model.service.food_service import FoodService


class FoodController:

    @staticmethod
    def add_food(request_data):
        try:
            title = request_data.get('title')
            price = request_data.get('price')
            duration = request_data.get('duration')
            description = request_data.get('description')
            status = request_data.get('status', True)

            food = FoodService.save(title, price, duration, description, status)
            return {"success": True, "food": food}, 201
        except Exception as e:
            return {"success": False, "error": str(e)}, 400

    @staticmethod
    def update_food(food_id, request_data):
        try:

            food = FoodService.find_by_id(food_id)
            if not food:
                return {"success": False, "error": "Food not found"}, 404

            food.title = request_data.get('title', food.title)
            food.price = request_data.get('price', food.price)
            food.duration = request_data.get('duration', food.duration)
            food.description = request_data.get('description', food.description)
            food.status = request_data.get('status', food.status)

            updated_food = FoodService.edit(food)
            return {"success": True, "food": updated_food}, 200
        except Exception as e:
            return {"success": False, "error": str(e)}, 400

    @staticmethod
    def delete_food(food_id):
        try:
            FoodService.remove(food_id)
            return {"success": True, "message": "Food deleted successfully"}, 200
        except Exception as e:
            return {"success": False, "error": str(e)}, 400

    @staticmethod
    def get_food_by_id(food_id):
        try:
            food = FoodService.find_by_id(food_id)
            if not food:
                return {"success": False, "error": "Food not found"}, 404
            return {"success": True, "food": food}, 200
        except Exception as e:
            return {"success": False, "error": str(e)}, 400

    @staticmethod
    def get_all_foods():
        try:
            foods = FoodService.find_all()
            return {"success": True, "foods": foods}, 200
        except Exception as e:
            return {"success": False, "error": str(e)}, 400

    @staticmethod
    def search_food_by_title(title):
        try:
            foods = FoodService.find_by_title(title)
            return {"success": True, "foods": foods}, 200
        except Exception as e:
            return {"success": False, "error": str(e)}, 400
