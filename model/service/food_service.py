from model.entity import Food
from model.repository.crud_repository import CrudRepository


class FoodService:
    repo = CrudRepository(Food)

    @classmethod
    def save(cls, title, price, duration, description, status=True):
        new_food = Food(title=title, price=price, duration=duration, description=description, status=status)
        return cls.repo.save(new_food)

    @classmethod
    def edit(cls, food):
        return cls.repo.edit(food)

    @classmethod
    def remove(cls, food_id):
        cls.repo.remove(food_id)
        return food_id

    @classmethod
    def find_by_id(cls, food_id):
        return cls.repo.find_by_id(food_id)

    @classmethod
    def find_all(cls):
        return cls.repo.find_all()

    @classmethod
    def find_by_title(cls, title):
        return cls.repo.find_by(Food._title.like(f"%{title}%"))
