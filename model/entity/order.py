from model.entity import *
from model.tools.validation import pattern_validator


class Order(Base):
    __tablename__ = "order_table"

    # table relations
    foods = relationship("Food", back_populates="order", cascade='all, delete-orphan')
    drinks = relationship("Drink", back_populates="order", cascade='all, delete-orphan')

    # table columns
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _amount = Column("amount", Integer, nullable=False)
    _discount = Column("discount", String(5), default=0)
    _pure_amount = Column("pure_amount", Integer, nullable=True)
    _date_time = Column("date", DateTime)

    # foreign columns
    _food = Column("food", String(20), nullable=False)
    _drink = Column("drink", String(20), nullable=False)

    def __init__(self, id, pure_amount, discount, amount):
        self._id = id
        self._pure_amount = pure_amount
        self._discount = discount
        self._amount = amount
        self.dt = datetime.now()

    # id getter and setter
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    # pure amount getter and setter
    @property
    def pure_amount(self):
        return self._pure_amount

    @pure_amount.setter
    @pattern_validator(r"^\$?(\d{1,3}(,\d{3})*|\d+)(\.\d{2})?$", "Invalid Amount")
    def pure_amount(self, pure_amount):
        self._pure_amount = pure_amount

    # discount setter and getter
    @property
    def discount(self):
        return self._discount

    @discount.setter
    @pattern_validator(r"^\d{1,3}%$", "Invalid Discount")
    def discount(self, discount=0):
        self._discount = discount

    # amount getter and setter
    @property
    def amount(self):
        return self._amount

    @amount.setter
    @pattern_validator(r"^\$?(\d{1,3}(,\d{3})*|\d+)(\.\d{2})?$", "Invalid Amount")
    def amount(self, amount):
        self._amount = amount
