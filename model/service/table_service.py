from model.entity import Table
from model.repository.crud_repository import CrudRepository


class TableService:
    repo = CrudRepository(Table)

    @classmethod
    def save(cls, table):
        cls.repo.save(table)
        return table

    @classmethod
    def edit(cls, table):
        cls.repo.edit(table)
        return table

    @classmethod
    def remove(cls, id):
        cls.repo.remove(id)
        return id

    @classmethod
    def find_all(cls):
        return cls.repo.find_all()

    @classmethod
    def find_empty_table(cls, is_empty):
        return cls.repo.find_by(Table.is_empty == is_empty)

    @classmethod
    def find_by_number(cls, number):
        return cls.repo.find_by(Table.number == number)
