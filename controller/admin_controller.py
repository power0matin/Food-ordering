from model.entity.admin import Admin
from model.service.admin_service import AdminService


class AdminController:

    @classmethod
    def save(cls, name, family, username, password, access_level):
        try:
            admin = Admin(name, family, username, password, access_level)
            AdminService.save(admin)
            return True, "Admin Saved."
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, name, family, username, password, access_level):
        try:
            admin = Admin(name, family, username, password, access_level)
            AdminService.edit(admin)
            return True, "Admin Edited."
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, id):
        try:
            AdminService.remove(id)
            return True, "Admin Removed."
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            return True, AdminService.find_all()
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            return True, AdminService.find_by_id(id)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_username(cls, username):
        try:
            return True, AdminService.find_by_username(username)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_username_password(cls, username, password):
        try:
            return True, AdminService.find_by_username_password(username, password)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_access_level(cls, access_level):
        try:
            return True, AdminService.find_by_access_level(access_level)
        except Exception as e:
            return False, str(e)
