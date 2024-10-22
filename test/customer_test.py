from controller import CustomerController
from view import CustomerView

#save
# CustomerController.save("ali", "alipour", "aidashmas77@gmail.com", "09111234567", "aida123", "aidash123")

#edit
# CustomerController.edit(id, "name", "family", "email", "phone", "username", "password")

#remove
#CustomerController.remove(id)

#find all
# all_customers = CustomerController.find_all()
# for customer in all_customers[1]:
#     print(f"ID: {customer.id}, Name: {customer.name}, Username: {customer.username}")

#find by id
# _, customer = CustomerController.find_by_id(1)
# if customer:
#     print(f"Found Customer: Name: {customer.name}, Username: {customer.username}")

#find by username
# CustomerController.find_by_username("ali")
# CustomerController.find_by_username_and_password("aida123", "aidash123")


CustomerView()