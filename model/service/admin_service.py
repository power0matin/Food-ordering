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
    def find_by(cls, by):
        return cls.repo.find_by(by)
