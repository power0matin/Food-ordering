from model.entity import Admin, and_
from model.repository import CrudRepository


class AdminService:
    repo = CrudRepository(Admin)

    @classmethod
    def save(cls, admin):
        return cls.repo.save(admin)

    @classmethod
    def edit(cls, admin):
        return cls.repo.edit(admin)

    @classmethod
    def remove(cls, id):
        return cls.repo.remove(id)

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
        return cls.repo.find_by(and_(Admin.username == username, Admin.password == password))

    @classmethod
    def find_by_access_level(cls, access_level):
        return cls.repo.find_by(Admin.access_level == access_level)
