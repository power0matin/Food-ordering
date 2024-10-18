from controller.table_controller import TableController

TableController.save("right", "mashad", "12")
TableController.save("left", "mashad", "12", True)
TableController.edit(1, "", "", "", False)
TableController.remove(1)
TableController.find_all()
TableController.find_empty_table()

TableController.find_by_number(2)

