from model.tools import validation
from sqlalchemy import Column, Integer, String, Boolean


class Admin:
    __tablename__ = "admin_tbl"

    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _name = Column("name", String(50), nullable=False)
    _family = Column("family", String(50), nullable=False)
    _username = Column("username", String(30), nullable=False)
    _password = Column("password", String(40), nullable=False)
    _access_level = Column("access_level", Integer, nullable=False)

    def __init__(self, id, name, family, username, password, access_level):
        self.id = validation.id_validator(id)
        self._name = validation.name_validator(name)
        self._family = validation.family_validator(family)
        self.username = validation.username_validator(username)
        self.password = validation.password_validator(password)
        self.access_level = validation.access_level_validator(access_level)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = validation.id_validator(id)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = validation.name_validator(name)

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, family):
        self._family = validation.family_validator(family)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = validation.username_validator(username)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = validation.password_validator(password)

    @property
    def access_level(self):
        return self._access_level

    @access_level.setter
    def access_level(self, access_level):
        self._access_level = validation.access_level_validator(access_level)
