from model.service.table_service import TableService
from model.entity.table import Table
from model.tools.decorators import exception_handling


class TableController:

    @classmethod
    @exception_handling
    def save(cls, title, location, number, is_empty):
        table = Table(None, title, location, number, is_empty)
        TableService.save(table)
        return "Table saved successfully"

    @classmethod
    @exception_handling
    def edit(cls, id, title, location, number, is_empty):
        table = Table(id, title, location, number, is_empty)
        TableService.edit(table)
        return "Table edited successfully"

    @classmethod
    @exception_handling
    def remove(cls, id):
        TableService.remove(id)
        return "Table removed successfully"

    @classmethod
    @exception_handling
    def find_all(cls):
        return TableService.find_all()


    @classmethod
    @exception_handling
    def find_empty_table(cls):
        return TableService.find_empty_table()

    @classmethod
    @exception_handling
    def find_by_number(cls, number):
        return TableService.find_by_number(number)
