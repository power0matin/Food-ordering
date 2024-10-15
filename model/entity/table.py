from model.entity import *
from model.tools.validation import pattern_validator
class Table():
    __tablename__ = "table_tbl"

    _id = Column("id",Integer, primary_key=True, autoincrement=True)
    _title = Column("title", String(30), nullable=False)
    _location = Column("location", String(30), nullable=False)
    _number = Column("number", Integer, nullable=False)
    _is_empty = Column("empty", Boolean, default=True )

    def __init__(self, id, title, location, number, is_empty):
        self.id = id
        self.title = title
        self.location = location
        self.number = number
        self.is_empty = is_empty

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def title(self):
        return self._title

    @title.setter
    @pattern_validator(r"^[a-zA-Z0-9\s]$","Invalid name")
    def title(self, title):
        self._title = title

    @property
    def location(self):
        return self._location

    @location.setter
    @pattern_validator(r"^[a-zA-Z\s]$","Invalid name")
    def location(self, location):
        self._location = location

    @property
    def number(self):
        return self._number

    @number.setter
    @pattern_validator(r"^[0-9]$","Invalid name")
    def number(self, number):
        self._number = number

    @property
    def is_empty(self):
        return self._is_empty

    @is_empty.setter
    def is_empty(self, is_empty):
        self._is_empty = is_empty











