from model.entity import *


class Order(Base):
    __tablename__ = "order_table"
    _id = Column("Id", Integer, primary_key=True, autoincrement=True)
    _amount = Column("Amount", Integer, nullable=False)
    _discount = Column("Discount", Float, default=0)
    _pure_amount = Column("Pure Amount", Integer, default=None, nullable=True)
    _date_time = Column("Date", DateTime)

    def __init__(self, order_id, pure_amount, discount, amount):
        self._id = order_id
        self._pure_amount = pure_amount
        self._discount = discount
        self._amount = amount

    @property
    def order_id(self):
        return self._id

    @order_id.setter
    def order_id(self, order_id):
        self._id = Validation.id_validator(order_id, "Invalid Id")

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = OrderValidation.amount_validator(amount, "Invalid Amount")

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount=0):
        self._discount = OrderValidation.discount_validator(discount, "Invalid Discount")

    @property
    def pure_amount(self):
        return self._pure_amount

    @pure_amount.setter
    def pure_amount(self, pure_amount):
        self._pure_amount = OrderValidation.amount_validator(pure_amount, "Invalid Amount")


# Be sure to instantiate correctly
order_1 = Order(1, 42, 0.12, 42)