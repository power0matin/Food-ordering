from model.entity import *


class Order(Base):

    __tablename__ = "order_table"
    _id = Column("ID", Integer, primary_key=True, autoincrement=True)
    _pure_amount = Column("Pure Amount", Integer, default=None, nullable=True)
    _discount = Column("Discount", Float, default=0)
    _amount = Column("Amount", Integer, nullable=False)
    _date_time = Column("Date", DateTime)

    def __init__(self, id, pure_amount, discount, amount):
        self.id = id
        self.pure_amount = pure_amount
        self.discount = discount
        self.amount = amount

    @property
    def id(self):
        return self._id

    @id.setter
    def order_id(self, id):
        self._id = Validation.id_validator(id, "Invalid Id")

    @property
    def pure_amount(self):
        return self._pure_amount

    @pure_amount.setter
    def pure_amount(self, pure_amount=amount):
        self.pure_amount = OrderValidation.amount_validator(pure_amount, "Invalid Amount")

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount=0):
        self._discount = OrderValidation.discount_validator(discount, "Invalid Discount")

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = OrderValidation.amount_validator(amount, "Invalid Amount")


order_1 = Order(1, 42, 0.12, 42)
