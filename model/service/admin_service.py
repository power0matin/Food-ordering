from model.entity.admin import Admin
from model.repository.crud_repository import CrudRepository


class AdminService:
    repo = CrudRepository(Admin)

    @classmethod
    def save(cls, admin):
        cls.repo.save(admin)
        return admin

    @classmethod
    def edit(cls, admin):
        cls.repo.edit(admin)
        return admin

    @classmethod
    def remove(cls, id):
        cls.repo.remove(id)
        return id

    @classmethod
    def find_all(cls):
        return cls.repo.find_all()

    @classmethod
    def find_by_id(cls, id):
        return cls.repo.find_by_id(id)

    @classmethod
    def find_by(cls, find_statement):
        return cls.repo.find_by(find_statement)

    @classmethod
    def find_by_username(cls, username):
        return cls.repo.find_by(Admin.username == username)

    @classmethod
    def find_by_username_password(cls, username, password):
        return cls.repo.find_by((Admin.username == username) & (Admin.password == password))

    @classmethod
    def find_by_access_level(cls, access_level):
        return cls.repo.find_by(Admin.access_level == access_level)
