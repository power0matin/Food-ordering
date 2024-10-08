from model.entity.admin import Admin
from model.repository.crud_repository import CrudRepository


class AdminService:
    repo = CrudRepository(Admin)

    @classmethod
    def add(cls, username, password, name, family, access_level):
        new_admin = Admin(username=username, password=password, name=name, family=family, access_level=access_level)
        cls.repo.save(new_admin)
        return new_admin

    @classmethod
    def edit(cls, admin: Admin):
        cls.repo.edit(admin)
        return admin

    @classmethod
    def remove(cls, admin_id):
        cls.repo.remove(admin_id)
        return admin_id

    @classmethod
    def find_all(cls):
        return cls.repo.find_all()

    @classmethod
    def find_by_id(cls, admin_id):
        return cls.repo.find_by_id(admin_id)

    @classmethod
    def find_by(cls, find_statement):
        return cls.repo.find_by(find_statement)
