from model.entity import Table
from model.service import TableService
from model.tools import exception_handling


class TableController:

    @classmethod
    @exception_handling
    def save(cls, title, location, number, is_empty):
        table = Table(None, title, location, number, is_empty)
        TableService.save(table)
        return table

    @classmethod
    @exception_handling
    def edit(cls, id, title, location, number, is_empty):
        table = Table(id, title, location, number, is_empty)
        TableService.edit(table)
        return table

    @classmethod
    @exception_handling
    def remove(cls, id):
        return TableService.remove(id)

    @classmethod
    @exception_handling
    def find_all(cls):
        return TableService.find_all()


    @classmethod
    @exception_handling
    def find_by_id(cls,id):
        return TableService.find_by_id(id)

    @classmethod
    @exception_handling
    def find_empty_tables(cls):
        return TableService.find_empty_table(Table.is_empty == True)

    @classmethod
    @exception_handling
    def find_by_number(cls, number):
        return TableService.find_by_number(number)
