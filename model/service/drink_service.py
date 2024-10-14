from model.entity.drink import Drink
from model.repository.crud_repository import CrudRepository

class DrinkService:
    repo = CrudRepository(Drink)

    @classmethod
    def save(cls, title, price, duration, status=True):
        new_drink = Drink(title=title, price=price, duration=duration, status=status)
        return cls.repo.save(new_drink)

    @classmethod
    def edit(cls, drink):
        return cls.repo.edit(drink)

    @classmethod
    def remove(cls, drink_id):
        cls.repo.remove(drink_id)
        return drink_id

    @classmethod
    def find_by_id(cls, drink_id):
        return cls.repo.find_by_id(drink_id)

    @classmethod
    def find_all(cls):
        return cls.repo.find_all()

    @classmethod
    def find_by_title(cls, title):
        return cls.repo.find_by(drink._title.like(f"%{title}%"))
