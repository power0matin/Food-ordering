# model/repository/crud_repository.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("mysql+pymysql://root:root123@localhost:3306/mft")

Session = sessionmaker(bind=engine)
session = Session()


class CrudRepository:
    def __init__(self, class_name):
        self.class_name = class_name

    def save(self, entity):
        session.add(entity)
        session.commit()
        session.refresh(entity)
        return entity.to_tuple()

    def edit(self, entity):
        session.merge(entity)
        session.commit()
        return entity.to_tuple()

    def remove(self, id):
        entity = session.get(self.class_name, id)
        if entity:
            session.delete(entity)
            session.commit()
            return entity.to_tuple()
        return None

    def find_all(self):
        entity_list = session.query(self.class_name).all()
        return [entity.to_tuple() for entity in entity_list]

    def find_by_id(self, id):
        entity = session.get(self.class_name, id)
        return entity.to_tuple() if entity else None

    def find_by(self, find_statement):
        entity_list = session.query(self.class_name).filter(find_statement).all()
        return [entity.to_tuple() for entity in entity_list]
