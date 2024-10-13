from model.service.table_service import TableService
from model.entity.table import Table

class TableController:

    @classmethod
    def save(cls, title, location, number):
        try:
            table = Table(None,title, location, number , is_empty)
            TableService.save(table)
            return True, "Table saved successfully"
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, id, title, location, number):
        try:
            table = Table(id,title, location, number , is_empty)
            TableService.edit(table)
            return True, "Table edited successfully"
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, id):
        try:
            table.remove(id)
            return True, "Table removed successfully"
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            return True, TableService.find_all()
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            return True,TableService.find_by_id(id)
        except Exception as e:
            return False, str(e)
