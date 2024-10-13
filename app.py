from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists
from controller.admin_controller import AdminController
from model.entity.base import Base

connection_string = "mysql+pymysql://root:root123@localhost:3306/mft"
if not database_exists(connection_string):
    create_database(connection_string)

engine = create_engine(connection_string)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

AdminController.save()

u = AdminController.find_by_id(1)
print(u)
