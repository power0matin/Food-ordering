from model.entity import Food
from model.repository import CrudRepository


class FoodService:
    repo = CrudRepository(Food)

    @classmethod
    def save(cls, food):
        return cls.repo.save(food)

    @classmethod
    def edit(cls, food):
        return cls.repo.edit(food)

    @classmethod
    def remove(cls, id):
        return cls.repo.remove(id)

    @classmethod
    def find_all(cls):
        return cls.repo.find_all()

    @classmethod
    def find_by_id(cls, id):
        return cls.repo.find_by_id(id)

    @classmethod
    def find_by(cls, find_statement):
        return cls.repo.find_by(find_statement)

    @classmethod
    def find_by_title(cls, title):
        return cls.repo.find_by(Food._title.like(f"%{title}%"))

    @classmethod
    def find_by_status(cls, status):
        return cls.repo.find_by(Food.available == status)
