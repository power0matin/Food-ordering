from model.entity import Table
from model.repository import CrudRepository


class TableService:
    repo = CrudRepository(Table)

    @classmethod
    def save(cls, table):
        return cls.repo.save(table)

    @classmethod
    def edit(cls, table):
        return cls.repo.edit(table)

    @classmethod
    def remove(cls, id):
        return cls.repo.remove(id)

    @classmethod
    def find_all(cls):
        return cls.repo.find_all()

    @classmethod
    def find_empty_table(cls, is_empty):
        return cls.repo.find_by(Table.is_empty == is_empty)

    @classmethod
    def find_by_number(cls, number):
        return cls.repo.find_by(Table.number == number)
