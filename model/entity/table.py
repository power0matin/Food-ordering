from sqlalchemy import Column, Integer, String, Boolean
from model.entity.base import Base
from model.tools.table_validation import TableValidation
class Table(Base):
    __tablename__ = 'table_tbl'
    _id = Column(Integer, primary_key=True, autoincrement=True)
    _title = Column("title", String, nullable=False)
    _location = Column("location", nullable=False)
    _number = Column("number", Integer, nullable=False)
    _is_empty = Column("empty", Boolean)

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
    def title(self, title):
        self._title = TableValidation.title_validator(title, "invalid Amount")

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        self._location = TableValidation.location_validator(location, "invalid Amount")

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        self._number = TableValidation.number_validator(number, "invalid Amount")

    @property
    def is_empty(self):
        return self._is_empty

    @is_empty.setter
    def is_empty(self, is_empty):
        self._is_empty = is_empty











