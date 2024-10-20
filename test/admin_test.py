from controller import AdminController

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
admin = AdminController.find_by_id(admin_id)[1]
if admin:
    print(f"Found Admin: Name: {admin.name}, Username: {admin.username}")

# Find by username
username = "aliaaaa"
status, admin_by_username = AdminController.find_by_username(username)
if status and admin_by_username:
    for admin in admin_by_username:
        print(f"ID: {admin.id}, Name: {admin.name}, Username: {admin.username}")
