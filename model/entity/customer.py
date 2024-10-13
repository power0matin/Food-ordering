#customer - Aida Shams
#UNFINISHED
from model.entity.base import Base
from model.tools. validation import Validation
from sqlalchemy import Column, Integer, String

#Customer : id, Name, Family, Email, Phone, Username, Password

class Customer(Base):
    __tablename__ = "customer_tbl"

    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _name = Column("name", String(20), nullable=False)
    _family = Column("family", String(20), nullable=False)
    _email = Column("email", String(50), nullable=False)
    _phone = Column("phone", Integer, default=[0])
    _username = Column("username", String(20), nullable=False)
    _password = Column("password", Integer , default="")

    def __init__(self, id, name, family, email, phone, username, password):
        self.id = id
        self.name = name
        self.family = family
        self.email = email
        self.phone = phone
        self.username = username
        self.password = password

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = Validation.id_validator(id, "Invalid Id")


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = Validation.name_validator(name, "Invalid Name!")


    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, family):
        self._family = Validation.family_validator(family, "Invalid Family!")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
       self._email = Validation.email_validator(email, "Invalid Email!")


    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = Validation.phone_validator(phone, "Invalid Phone!")


    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = Validation.username_validator(username, "Invalid Username!")


    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = Validation.password_validator(password, "Invalid Password!")