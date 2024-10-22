from controller import AdminController
from view import AdminView

# Save
# status , admin = AdminController.save("ali", "alipour", "aliaaaa", "aliaaa123", "11")

# # Edit
#status, admin =  AdminController.edit(admin_id, "Ali", "Alipour", "aliupdated", "newpassword123", 1111)

# # Remove
#status, old_admin = AdminController.remove(admin_id)

# # Find all
# status, all_admins = AdminController.find_all()
# print(all_admins)

# # Find by ID
#status, admin = AdminController.find_by_id(admin_id)[1]
# print(admin)

# # Find by username
# username = "aliaaaa"
# status, admin_by_username = AdminController.find_by_username(username)
# if status and admin_by_username:
#     for admin in admin_by_username:
#         print(f"ID: {admin.id}, Name: {admin.name}, Username: {admin.username}")

AdminView()
