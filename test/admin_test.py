from controller.admin_controller import AdminController

# Save
AdminController.save("ali", "alipour","aliaaaa","aliaaa123", 1111)

admin_id = 1

# Edit
AdminController.edit(admin_id, "Ali", "Alipour", "aliupdated", "newpassword123", 1111)

# Remove
AdminController.remove(admin_id)

# Find all
all_admins = AdminController.find_all()
for admin in all_admins[1]:
    print(f"ID: {admin.id}, Name: {admin.name}, Username: {admin.username}")

admin_id = 1

# Find by ID
admin = AdminController.find_by_id(admin_id)
print(f"Found Admin: Name: {admin[1].name}, Username: {admin[1].username}")

# Find by username
username = "aliaaaa"
admin_by_username = AdminController.find_by_username(username)
for admin in admin_by_username[1]:
    print(f"ID: {admin.id}, Name: {admin.name}, Username: {admin.username}")