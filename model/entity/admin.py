from model.entity import *


class Admin(Base):
    __tablename__ = "admin_tbl"

    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _name = Column("name", String(50), nullable=False)
    _family = Column("family", String(50), nullable=False)
    _username = Column("username", String(30), nullable=False)
    _password = Column("password", String(40), nullable=False)
    _access_level = Column("access_level", Integer, nullable=False)

    def __init__(self, id, name, family, username, password, access_level):
        self.id = id
        self._name = name
        self._family = family
        self.username = username
        self.password = password
        self.access_level = access_level

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
        self._name = Validation.name_validator(name, "Invalid name")

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, family):
        self._family = Validation.family_validator(family, "Invalid family")

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = Validation.username_validator(username, "Invalid username")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = Validation.password_validator(password, "Invalid password")

    @property
    def access_level(self):
        return self._access_level

    @access_level.setter
    def access_level(self, access_level):
        # self._access_level = Validation.access_level_validator(access_level, "Invalid Level")
        self._access_level = access_level
