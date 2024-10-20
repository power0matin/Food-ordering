from controller.order_controller import *
from model.service.order_service import *
from model.entity.order import *

# todo : test is not complete
# OrderController.save(1, 42, 0, 213)

OrderController.save(123,"40%", 123)
OrderController.edit(125,123, "30%", 123)
OrderController.remove(1)
OrderController.find_all()
OrderController.find_by_id(1)
