from model.entity import *


class Payment(Base):
    __tablename__ = "payment_tbl"

    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _amount = Column("amount", Float, nullable=False)
    _date_time = Column("date_time", DateTime, default=datetime.now)
    _payment_type = Column("payment_type", String(30), nullable=False)
    _description = Column("description", String(255), nullable=True)
    _order = Column("order", Integer, nullable=False)

    def __init__(self, id, amount, payment_type, description, order):
        self.id = id
        self.amount = amount
        self.payment_type = payment_type
        self.description = description
        self.order = order
        self.dt = datetime.now()

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        if amount <= 0:
            raise ValueError("Invalid Amount.")
        self._amount = amount

    @property
    def date_time(self):
        return self._date_time

    @property
    def payment_type(self):
        return self._payment_type

    @payment_type.setter
    def payment_type(self, payment_type):
        if not payment_type:
            raise ValueError("Invalid Payment Type.")
        self._payment_type = payment_type

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def order(self):
        return self._order

    @order.setter
    def order(self, order):
        if order <= 0:
            raise ValueError("Invalid Order.")
        self._order = order
