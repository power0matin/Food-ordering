from model.entity import *
from model.tools.validation import Validation

class Food(Base):
    __tablename__ = "food_tbl"

    id = Column(Integer, primary_key=True, autoincrement=True)
    _title = Column("title", String(50), nullable=False)
    _description = Column("description", String(100), nullable=False)
    _price = Column("price", Float, nullable=False)
    _duration = Column("duration", Integer, nullable=False)
    _size = Column("size", String(10), nullable=False)
    _available = Column("available", Boolean, default=True)

    def __init__(self, id, title, description, price, duration, size, available=True):
        self.id = id
        self.title = title
        self.description = description
        self.price = price
        self.duration = duration
        self.size = size
        self.available = available

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = Validation.title_validator(title, "Invalid Title!")

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = Validation.description_validator(description, "Invalid Description!")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = Validation.price_validator(price, "Invalid Price!")

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration):
        self._duration = Validation.duration_validator(duration, "Invalid Duration!")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = Validation.size_validator(size, "Invalid Size!")

    @property
    def available(self):
        return self._available

    @available.setter
    def available(self, available):
        self._available = available
