from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists, drop_database
from controller.admin_controller import AdminController
from controller.customer_controller import CustomerController
from controller.payment_controller import PaymentController
from controller.table_controller import TableController
from model.entity import Base
from view.admin_view import AdminView
from view.customer_view import CustomerView
from view.payment_view import PaymentView

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
#
AdminController.save("matin", "shahabadi", "powermatin", "abcd1234", "1")
# #
# u = AdminController.find_by_id(1)
# print(u)
# #
# # costumer app test
CustomerController.save("aida", "shams", "asHe77@gmail.com", "09114567893", "aidaaa", "aida1234")
CustomerView()
# todo: '"tuple" object has no attribute "id"'
# # payment app test
#PaymentController.save(3, "online", "blah blah", "drink")
#PaymentView()
# #
# TableController.save("table1", "right", 2, True)
#AdminView()