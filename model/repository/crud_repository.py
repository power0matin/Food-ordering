from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists
from model.entity.base import Base

# تنظیمات اتصال به دیتابیس
connection_string = "mysql+pymysql://root:root123@localhost:3306/mft"
if not database_exists(connection_string):
    create_database(connection_string)

engine = create_engine(connection_string, echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


class CrudRepository:
    def __init__(self, class_name):
        self.class_name = class_name

    def save(self, entity):
        try:
            session.add(entity)
            session.commit()
            session.refresh(entity)
            return entity
        except Exception as e:
            session.rollback()
            raise e

    def edit(self, entity):
        try:
            session.merge(entity)
            session.commit()
            return entity
        except Exception as e:
            session.rollback()
            raise e

    def remove(self, admin_id):
        try:
            entity = session.get(self.class_name, admin_id)
            session.delete(entity)
            session.commit()
            return entity
        except Exception as e:
            session.rollback()
            raise e

    def find_all(self):
        try:
            entity_list = session.query(self.class_name).all()
            return entity_list
        except Exception as e:
            raise e

    def find_by_id(self, admin_id):
        try:
            entity = session.get(self.class_name, admin_id)
            return entity
        except Exception as e:
            raise e

    def find_by(self, find_statement):
        try:
            entity = session.query(self.class_name).filter(find_statement).all()
            return entity
        except Exception as e:
            raise e

    def find_by_username(self, username):
        try:
            entity = session.get(self.class_name, username)
            return entity
        except Exception as e:
            raise e