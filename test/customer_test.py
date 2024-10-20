# customer test - Aida Shams
from model.entity import customer
from model.entity.customer import Customer
from controller.customer_controller import CustomerController

# customer = Customer(123, "ai0da", "sH9ams", "aidashmas77mail.com", "091aa456789", "aida-123", "aidas-123")

# print(customer)


CustomerController.save("ali", "alipour", "aidashmas77@gmail.com", "09111234567", "aida123", "aidash123")

#find all
all_customers = CustomerController.find_all()
for Customer in all_customers[1]:
    print(f"ID: {Customer.id}, Name: {Customer.name}, Username: {Customer.username}")

#find by id
customer = CustomerController.find_by_id(1)
if customer:
    print(f"Found Customer: Name: {Customer.name}, Username: {Customer.username}")

#find by username
CustomerController.find_by_username("ali")
CustomerController.find_by_username_and_password("aida123", "aidash123")
