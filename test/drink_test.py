from controller import DrinkController
from view import DrinkView

DrinkController.save("Coca Cola", 1.5, 250, "medium")

# drink_id = 1

#
# DrinkController.edit(1, "Pepsi", 1.2, 300, "medium drink updated")
#
#
# DrinkController.remove(drink_id)
#
#
# all_drinks = DrinkController.find_all()
# for drink in all_drinks[1]:
#     print(f"ID: {drink.id}, Title: {drink.title}, Price: {drink.price}, Size: {drink.size}, Duration: {drink.duration}")
#
# drink_id = 1
# drink = DrinkController.find_by_id(drink_id)[1]
# if drink:
#     print(f"Found Drink: Title: {drink.title}, Price: {drink.price}, Size: {drink.size}, Duration: {drink.duration}")
#
# title = "Coca Cola"
# status, drinks_by_title = DrinkController.find_by_title(title)
# if status and drinks_by_title:
#     for drink in drinks_by_title:
#         print(f"ID: {drink.id}, Title: {drink.title}, Price: {drink.price}, Size: {drink.size}, Duration: {drink.duration}")
DrinkView()