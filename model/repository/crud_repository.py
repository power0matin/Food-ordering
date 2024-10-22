from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists, drop_database
from model.entity import *

connection_string = "mysql+pymysql://root:root123@localhost:3306/mft"
if database_exists(connection_string):
    drop_database(connection_string)
create_database(connection_string)

engine = create_engine(connection_string)

try:
    Base.metadata.drop_all(engine)
except:
    pass
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
        entity = session.query(self.class_name).where(find_statement).all()
        return entity