from controller.table_controller import TableController
from view.table_view import TableView

# todo : test failes

# Save +
TableController.save("table3", "right", 3, True)

# Edit +
# TableController.edit(14, "22", "left", 13, False)

# Remove +
# TableController.remove(2)

# Find all +
# table_findall = TableController.find_all()
# for table in table_findall[1]:
#   print(f"title: {table.title}, location: {table.location}, number: {table.number}, is_empty: {table.is_empty}")

# Find Empty Table

# TableController.find_empty_table()

# Find By Number

# TableController.find_by_number(2)


TableView()