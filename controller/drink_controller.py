from model.service.drink_service import _service, drink
import DrinkService


class DrinkController:

    @staticmethod
    def add_drink(request_data):
        try:
            title = request_data.get('title')
            price = request_data.get('price')
            duration = request_data.get('duration')
            status = request_data.get('status', True)
            size = request_data.get('size')

            drink = DrinkService.save(title, price, duration, status,size)
            return {"success": True, "food": food}, 201
        except Exception as e:
            return {"success": False, "error": str(e)}, 400

    @staticmethod
    def update_drink(drink_id, request_data):
        try:

            drink = DrinkService.find_by_id(drink_id)
            if not food:
                return {"success": False, "error": "drink not found"}, 404

            drink.title = request_data.get('title', drink.title)
            drink.price = request_data.get('price', drink.price)
            drink.duration = request_data.get('duration', drink.duration)
            drink.status = request_data.get('status', drink.status)
            drink.size = request_data.get('size', drink.size)

            updated_drink = DrinkService.edit(drink)
            return {"success": True, "drink": updated_drink}, 200
        except Exception as e:
            return {"success": False, "error": str(e)}, 400

    @staticmethod
    def delete_drink(drink_id):
        try:
            DrinkService.remove(drink_id)
            return {"success": True, "message": "Drink deleted successfully"}, 200
        except Exception as e:
            return {"success": False, "error": str(e)}, 400

    @staticmethod
    def get_drink_by_id(drink_id):
        try:
            drink = DrinkService.find_by_id(drink_id)
            if not drink:
                return {"success": False, "error": "Drink not found"}, 404
            return {"success": True, "drink": drink}, 200
        except Exception as e:
            return {"success": False, "error": str(e)}, 400

    @staticmethod
    def get_all_drink():
        try:
            drinks = DrinkService.find_all()
            return {"success": True, "drinks": drinks}, 200
        except Exception as e:
            return {"success": False, "error": str(e)}, 400

    @staticmethod
    def search_food_by_title(title):
        try:
            drinks = DrinkService.find_by_title(title)
            return {"success": True, "drinks": drinks}, 200
        except Exception as e:
            return {"success": False, "error": str(e)}, 400
