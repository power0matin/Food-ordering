from controller.drink_controller import DrinkController

# todo : what is size? str ?
# todo : what is size? str ?
# todo : error
# DrinkController.get_all_drinks()
# todo error
# DrinkController.search_drink_by_title("Pepsi")
DrinkController.save("Pepsi", 3.0, 300, "integer", "Large")
drink_id = 1

DrinkController.edit(drink_id, "Pepsi", 6.0, 9.99, "integer", "Medium")
drink_id = 1

DrinkController.remove(drink_id)

all_drinks = DrinkController.find_all()
for drink in all_drinks[1]:
    print(f"ID: {drink}.id, Title: {drink}.title, Price: {drink}.price, Size: {drink}.size")

drink_id = 1
drink = DrinkController.find_by_id(drink_id)[1]
if drink:
    print(f"Found Drink: Title: {drink.title}, Price: {drink.price}, Size: {drink.size}")

title = "Drink"
status, drink_by_title = DrinkController.find_by_title(title)
if status and drink_by_title:
    for drink in drink_by_title:
        print(f"ID: {drink.id}, Title: {drink.title}, Price: {drink.price}, Size: {drink.size}")


