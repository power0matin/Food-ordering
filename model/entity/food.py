#under_review

from sqlalchemy import Column, Integer, String, Float, Boolean
from model.entity.base import Base
from model.tools.food_validation import FoodValidation

class Food(Base):
    __tablename__ = "food_tbl"

    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _title = Column("title", String(50), nullable=False)
    _description = Column("description", String(100), nullable=False)
    _price = Column("price", Float, nullable=False)
    _duration = Column("duration", Integer, nullable=False)
    _size = Column("size", String(10), nullable=False)
    _available = Column("available", Boolean, default=True)

    def __init__(self, food_id, title, description, price, duration, size, available=True):
        self.food_id = food_id
        self.title = title
        self.description = description
        self.price = price
        self.duration = duration
        self.size = size
        self.available = available

    @property
    def food_id(self):
        return self._id

    @food_id.setter
    def food_id(self, food_id):
        self._id = food_id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = FoodValidation.title_validator(title, "Invalid Title!")

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = FoodValidation.description_validator(description, "Invalid Description!")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = FoodValidation.price_validator(price, "Invalid Price!")

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration):
        self._duration = FoodValidation.duration_validator(duration, "Invalid Duration!")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = FoodValidation.size_validator(size, "Invalid Size!")

    @property
    def available(self):
        return self._available

    @available.setter
    def available(self, available):
        self._available = available