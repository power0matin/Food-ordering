from controller.food_controller import FoodController

# todo : error
# save a new food
FoodController.save("Pizza", "Delicious cheese pizza", 12.99, 30, "Large")

food_id = 1

# todo : error
# edit the food item
FoodController.edit(food_id, "Burger", "Juicy beef burger", 9.99, 20, "Medium", True)
food_id = 1

# remove the food item
FoodController.remove(food_id)

# todo : error
all_foods = FoodController.find_all()
for food in all_foods[1]:
    print(f"ID: {food.id}, Title: {food.title}, Price: {food.price}, Size: {food.size}")

# todo : error
food_id = 1
food = FoodController.find_by_id(food_id)[1]
if food:
    print(f"Found Food: Title: {food.title}, Price: {food.price}, Size: {food.size}")

# todo : error
title = "Pizza"
status, food_by_title = FoodController.find_by_title(title)
if status and food_by_title:
    for food in food_by_title:
        print(f"ID: {food.id}, Title: {food.title}, Price: {food.price}, Size: {food.size}")
