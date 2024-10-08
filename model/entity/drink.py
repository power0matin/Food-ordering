from sqlalchemy import Column, Integer, String, Float, Boolean
from model.entity.base import Base
from model.tools.drink_validation import DrinkValidation

class drink(Base):
    __tablename__ = "drink_tbl"

    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _title = Column("title", String(50), nullable=False)
    _price = Column("price", Float, nullable=False)
    _duration = Column("duration", Integer, nullable=False)
    _size = Column("size", String(10), nullable=False)
    _available = Column("available", Boolean, default=True)

    def __init__(self, drink_id, title, price, duration, size, available=True):
        self.drink_id = drink_id
        self.title = title
        self.price = price
        self.duration = duration
        self.size = size
        self.available = available

    @property
    def drink_id(self):
        return self._id

    @drink_id.setter
    def drink_id(self, drink_id):
        self._id = drink_id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = DrinkValidation.title_validator(title, "Invalid Title!")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = DrinkValidation.price_validator(price, "Invalid Price!")

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration):
        self._duration = DrinkValidation.duration_validator(duration, "Invalid Duration!")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = DrinkValidation.size_validator(size, "Invalid Size!")

    @property
    def available(self):
        return self._available

    @available.setter
    def available(self, available):
        self._available = available
