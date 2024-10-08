#customer - Aida Shams
#UNFINISHED
from model.entity.base import Base
from model.tools.customer_validation import CustomerValidation
from sqlalchemy import Column, Integer, String


class Customer(Base):
    __tablename__ = "customer_tbl"

    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _name = Column("name", String(20), nullable=False)
    _family = Column("family", String(20), nullable=False)
    _username = Column("username", String(20), nullable=False)
    _password = Column("password", Integer , default="")

    def __init__(self, customer_id, name, family, username, password):
        self.customer_id = customer_id
        self.name = name
        self.family = family
        self.username = username
        self.password = password

    @property
    def customer_id(self):
        return self._id

    @customer_id.setter
    def customer_id(self, customer_id):
        self._id = customer_id


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = CustomerValidation.name_validator(name, "Invalid Name!")


    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, family):
        self._family = CustomerValidation.family_validator(family, "Invalid Family!")


    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = CustomerValidation.username_validator(username, "Invalid Username!")


    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = CustomerValidation.password_validator(password, "Invalid Password!")