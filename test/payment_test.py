from controller.payment_controller import PaymentController
from model.entity import Payment

# Save
# todo : error
# PaymentController.save()

payment_id = 1

# Edit
# todo : error
PaymentController.edit(payment_id, )

# Remove
PaymentController.remove(payment_id)

# Find all
all_payments = PaymentController.find_all()
for payment in all_payments[1]:
    print(f"ID: {payment.id}, Amount: {payment.amount}, Payment Type: {payment.payment_type}")

#find by id
payment = PaymentController.find_by_id(1)
if payment:
    print(f"Found Payment: Amount: {Payment.amount}, Payment Type: {Payment.payment_type}")
