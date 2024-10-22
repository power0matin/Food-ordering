from controller.table_controller import TableController

# todo : test failes

# Save
#TableController.save("table1", "right", 2, True)

table_id = 1

# Edit
#TableController.edit(1, "22", "left", 13, False)

# Remove
TableController.remove(table_id)

# Find all
table_findall = TableController.find_all()
for table in table_findall[1]:
   print(f"title: {table.title}, location: {table.location}, number: {table.number}, is_empty: {table.is_empty}")

# Find Empty Table

# TableController.find_empty_table()

#Find By Number

# TableController.find_by_number(2)


