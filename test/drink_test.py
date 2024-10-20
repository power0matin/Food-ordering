from model.entity.drink import Drink
from controller.drink_controller import DrinkController

# todo : what is size? str ?
drink = Drink(1, "Cola", 3.5, 250, "Refres", True)

print(drink)

# todo : what is size? str ?
# todo : error
DrinkController.add_drink("Pepsi", 3.0, 300, "Pepsi", True)

# DrinkController.get_all_drinks()

DrinkController.get_drink_by_id(1)

# todo error
# DrinkController.search_drink_by_title("Pepsi")

DrinkController.search_drink_by_title_and_status("Pepsi", True)