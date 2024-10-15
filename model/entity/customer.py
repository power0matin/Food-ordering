#customer - Aida Shams
#UNFINISHED
from model.entity import *
from model.tools.validation import pattern_validator


#Customer : id, Name, Family, Email, Phone, Username, Password

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

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = Validation.pattern_validator(name, "^[a-zA-Z\s]{3,}$", "Invalid name")


    @property
    def family(self):
        return self._family


    @family.setter
    @pattern_validator("[a-zA-Z]{3,}", "Invalid Family")
    def family(self, family):
        self._family = family

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