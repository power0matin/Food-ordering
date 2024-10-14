from model.entity.drink import Drink
from controller.drink_controller import DrinkController

drink = Drink(1, "Cola", 3.5, 250, "Refreshing cola drink", True)

print(drink)

DrinkController.add_drink("Pepsi", 3.0, 300, "Pepsi with rich flavor", True)

DrinkController.get_all_drinks()

DrinkController.get_drink_by_id(1)

DrinkController.search_drink_by_title("Pepsi")

DrinkController.search_drink_by_title_and_status("Pepsi", True)