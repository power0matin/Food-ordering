from sqlalchemy import Column, Integer, String, Float
from model.entity.base import Base
from model.tools.food_validation import FoodValidation

class Food(Base):
    __tablename__ = "food_tbl"

    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _name = Column("name", String(50), nullable=False)
    _description = Column("description", String(100), nullable=False)
    _price = Column("price", Float, nullable=False)

    def __init__(self, food_id, name, description, price):
        self.food_id = food_id
        self.name = name
        self.description = description
        self.price = price

    @property
    def food_id(self):
        return self._id

    @food_id.setter
    def food_id(self, food_id):
        self._id = food_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = FoodValidation.name_validator(name, "Invalid Food Name!")

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