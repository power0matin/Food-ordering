# customer - Aida Shams - using property\validator
# Customer : id, Name, Family, Email, Phone, Username, Password

from model.entity import *
from model.tools.validation import pattern_validator


class Customer(Base):
    __tablename__ = "customer_tbl"

    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _name = Column("name", String(20), nullable=False)
    _family = Column("family", String(20), nullable=False)
    _email = Column("email", String(50), nullable=False)
    _phone = Column("phone", String(50), nullable=False)
    _username = Column("username", String(20), nullable=False)
    _password = Column("password", String(20), nullable=False)

    def __init__(self, id, name, family, email, phone, username, password):
        self.id = id
        self.name = name
        self.family = family
        self.email = email
        self.phone = phone
        self.username = username
        self.password = password

    # id\validator
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    # name\validator
    @property
    def name(self):
        return self._name

    @name.setter
    @pattern_validator(r"^[a-zA-Z\s]{2,20}$", "Invalid Name!")
    def name(self, name):
        self._name = name

    # family\validator
    @property
    def family(self):
        return self._family

    @family.setter
    @pattern_validator(r"^[a-zA-Z\s]{2,20}$", "Invalid Family!")
    def family(self, family):
        self._family = family

    # email\validator
    @property
    def email(self):
        return self._email

    @email.setter
    @pattern_validator(r"^[a-zA-Z0-9]\w+@(gmail|yahoo).com$", "Invalid Email!")
    def email(self, email):
        self._email = email

    # phone\validator
    @property
    def phone(self):
        return self._phone

    @phone.setter
    @pattern_validator(r"^09[0-9]{9}$", "Invalid Phone!")
    def phone(self, phone):
        self._phone = phone

    # username\validator
    @property
    def username(self):
        return self._username

    @username.setter
    @pattern_validator(r"^[a-zA-Z0-9]{5,}$", "Invalid Username!")
    def username(self, username):
        self._username = username

    # password\validator
    @property
    def password(self):
        return self._password

    @password.setter
    @pattern_validator(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", "Invalid Password!")
    def password(self, password):
        self._password = password

#note to self: sqlalchemy.exc.InvalidRequestError: Table 'customer_tbl' is already defined for this MetaData instance.-
# -Specify 'extend_existing=True' to redefine options and columns on an existing Table object.