from model.entity.base import Base
from sqlalchemy import Column, Integer, DateTime, String


class Order(Base):
    __tablename__ = "order_table"

    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _amount = Column("amount", Integer, nullable=False)
    _discount = Column("discount", Integer, default=0)
    _pure_amount = Column("pure_amount", Integer, default=_amount)
    _date_time = Column("date_time", DateTime)

    def __init__(self, id,table, customer, amount, discount, pure_amount):
        self.id = id
        self.amount = amount
        self.discount = discount
        self.pure_amount = pure_amount

    @property
    def order_id(self):
        return self._id

    @order_id.setter
    def order_id(self, order_id):
        self._id = order_id

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount=0):
        self._discount = discount

    @property
    def pure_amount(self):
        return self._pure_amount

    @pure_amount.setter
    def pure_amount(self, pure_amount=amount):
        self.pure_amount = pure_amount
