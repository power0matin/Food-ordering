from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists
from controller.admin_controller import AdminController
from controller.customer_controller import CustomerController
from model.entity import Base
from view.customer_view import CustomerView
from view.payment_view import PaymentView

connection_string = "mysql+pymysql://root:root123@localhost:3306"
if not database_exists(connection_string):
    create_database(connection_string)

engine = create_engine(connection_string)

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

AdminController.save("matin", "shahabadi", "powermatin", "abcd1234", "1")

u = AdminController.find_by_id(1)
print(u)

#CustomerController.save("aida", "shams", "asHe77@gmail.com", "09114567893", "aidaaa", "aida1234")
#CustomerView()

PaymentView()