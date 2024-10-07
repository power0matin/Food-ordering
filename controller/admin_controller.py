from model.entity.admin import Admin
from model.service.admin_service import AdminService


class AdminController:

    @classmethod
    def save(cls, admin_id, name, email, password):
        try:
            admin = Admin(admin_id, name, email, password)
            AdminService.save(admin)
            return True, "Info: Admin Saved!"
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, admin_id, name, email):
        try:
            admin = Admin(admin_id, admin_id, name, email)
            AdminService.edit(admin)
            return True, "Admin Has Been Edited!"
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, admin_id):
        try:
            AdminService.remove(admin_id)
            return True, "Info: Admin Removed!"
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            return True, AdminService.find_all()
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_id(cls, admin_id):
        try:
            return True, AdminService.find_by_id(admin_id)
        except Exception as e:
            return False, str(e)
