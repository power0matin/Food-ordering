from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists
from model.entity.admin import Admin
from model.entity.base import Base

# Database connection settings
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
        session.add(entity)
        session.commit()
        session.refresh(entity)
        return entity

    def edit(self, entity):
        session.merge(entity)
        session.commit()
        return entity

    def remove(self, id):
        entity = session.get(self.class_name, id)
        if entity:
            session.delete(entity)
            session.commit()
            return entity
        return None

    def find_all(self):
        entity_list = session.query(self.class_name).all()
        return entity_list

    def find_by_id(self, id):
        entity = session.get(self.class_name, id)
        return entity

    def find_by(self, find_statement):
        entity = session.query(self.class_name).filter(find_statement).all()
        return entity

    def find_by_username(self, username):
        return self.find_by(username == username)

    def find_by_access_level(self, access_level):
        return self.find_by(access_level == access_level)

    def find_by_credentials(self, username, password):
        return self.find_by((username == username) & (Admin.password == password))

    def find_by_name(self, name):
        return self.find_by(Admin._name == name)

    def find_by_family(self, family):
        return self.find_by(Admin._family == family)
