#customer test - Aida Shams
from model.entity.customer import Customer
from controller.customer_controller import CustomerController

#customer = Customer(123, "ai0da", "sH9ams", "aidashmas77mail.com", "091aa456789", "aida-123", "aidas-123")

#print(customer)



CustomerController.save("ali", "alipour","aidashmas77@gmail.com","09111234567", "aida123", "aidash123")
CustomerController.find_all()
CustomerController.find_by_id(1)
CustomerController.find_by_username("ali")
CustomerController.find_by_username_and_password("aida123", "aidash123")
