from controller.food_controller import FoodController


FoodController.add_food("Pizza", 15.5, 30, "Delicious pizza", True)

food_id = 1

FoodController.update_food(food_id, "Cheese Pizza", 17.0, 35, "Updated description", True)

food_id = 1

FoodController.delete_food(food_id)


all_foods = FoodController.get_all_foods()


for food in all_foods[0]['foods']:
    print(f"ID: {food.id}, Title: {food.title}, Price: {food.price}")

food_id = 1

# find by id
food = FoodController.get_food_by_id(food_id)
print(f"Found Food: Title: {food[0]['food'].title}, Price: {food[0]['food'].price}")

# find by title
title = "Pizza"

foods = FoodController.search_food_by_title(title)
for food in foods[0]['foods']:
    print(f"ID: {food.id}, Title: {food.title}, Price: {food.price}")
