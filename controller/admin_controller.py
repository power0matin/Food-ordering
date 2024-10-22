from model.entity.admin import Admin
from model.service.admin_service import AdminService
from model.tools.decorators import exception_handling


class AdminController:

    @classmethod
    @exception_handling
    def save(cls, name, family, username, password, access_level):
        admin = Admin(None, name, family, username, password, access_level)
        AdminService.save(admin)
        return admin

    @classmethod
    @exception_handling
    def edit(cls, id, name, family, username, password, access_level):
        admin = Admin(id, name, family, username, password, access_level)
        AdminService.edit(admin)
        return admin

    @classmethod
    @exception_handling
    def remove(cls, id):
        old_admin = AdminService.remove(id)
        return old_admin

    @classmethod
    @exception_handling
    def find_all(cls):
        return True, AdminService.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        return True, AdminService.find_by_id(id)

    @classmethod
    @exception_handling
    def find_by_username(cls, username):
        return True, AdminService.find_by_username(username)

    @classmethod
    @exception_handling
    def find_by_username_password(cls, username, password):
        return True, AdminService.find_by_username_password(username, password)

    @classmethod
    @exception_handling
    def find_by_access_level(cls, access_level):
        return True, AdminService.find_by_access_level(access_level)
