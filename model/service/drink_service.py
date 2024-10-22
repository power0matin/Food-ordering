from model.entity import Drink
from model.repository.crud_repository import CrudRepository


class DrinkService:
    repo = CrudRepository(Drink)

    @classmethod
    def save(cls , drink):
        return cls.repo.save(new_drink)

    @classmethod
    def edit(cls, drink):
        return cls.repo.edit(drink)

    @classmethod
    def remove(cls, id):
        return cls.repo.remove(id)

    @classmethod
    def find_by_id(cls, id):
        return cls.repo.find_by_id(id)

    @classmethod
    def find_by(cls, find_statement):
        return cls.repo.find_by(find_statement)

    @classmethod
    def find_by_title(cls, title):
        return cls.repo.find_by(Drink.title.like(f"%{title}%"))

    @classmethod
    def find_by_status(cls, status):
        return cls.repo.find_by(Drink.status == status)