from model.entity import Admin
from model.service import AdminService
from model.tools import exception_handling


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
        print(admin)
        AdminService.edit(admin)
        return admin

    @classmethod
    @exception_handling
    def remove(cls, id):
        return AdminService.remove(id)

    @classmethod
    @exception_handling
    def find_all(cls):
        return AdminService.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        return AdminService.find_by_id(id)

    @classmethod
    @exception_handling
    def find_by_username(cls, username):
        return AdminService.find_by_username(username)

    @classmethod
    @exception_handling
    def find_by_username_password(cls, username, password):
        return AdminService.find_by_username_password(username, password)

    @classmethod
    @exception_handling
    def find_by_access_level(cls, access_level):
        return AdminService.find_by_access_level(access_level)
