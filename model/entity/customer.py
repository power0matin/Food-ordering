#customer - Aida Shams
#UNFINISHED
from model.entity.base import Base
from model.tools.customer_validation import CustomerValidation
from sqlalchemy import Column, Integer, String


class Customer(Base):
    __tablename__ = "customer_tbl"

    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _name = Column("name", String(20), nullable=False)
    _email = Column("email", String(20), nullable=False)
    _phone = Column("phone", Integer, default=0)

    def __init__(self, customer_id, name, email, phone):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone

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
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = CustomerValidation.email_validator(email, "Invalid Email!")

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = CustomerValidation.phone_validator(phone, "Invalid Phone Number!")