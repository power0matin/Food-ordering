from model.entity import *
from model.tools.validation import pattern_validator

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
    @pattern_validator(r"^[a-zA-Z\s]{2,20}$", "Invalid name")
    def name(self, name):
        self._name = name

    @property
    def family(self):
        return self._family

    @family.setter
    @pattern_validator(r"^[a-zA-Z\s]{2,20}$", "Invalid family")
    def family(self, family):
        self._family = family

    @property
    def username(self):
        return self._username

    @username.setter
    @pattern_validator(r"^[a-zA-Z\s]{5,}$", "Invalid username")
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    @pattern_validator(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", "Invalid password")
    def password(self, password):
        self._password = password

    @property
    def access_level(self):
        return self._access_level

    @access_level.setter
    @pattern_validator(r"^[0-9]{1,}$", "Invalid access_level")
    def access_level(self, access_level):
        self._access_level = access_level
