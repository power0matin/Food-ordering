#customer test - Aida Shams
from model.entity.customer import Customer


customer = Customer(123, "aida", "sams", "aidashmas77mail.com", "091aa456789", "aida-123", "aidas-123")
# validation works okay but shows None instead of message!!!(email, phone)
print(customer)
