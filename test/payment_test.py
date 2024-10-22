from controller.payment_controller import PaymentController
from model.entity import Payment
from view import PaymentView

# Save
PaymentController.save(3, "online", "blah blah", "pizza")

# payment_id = 1

# Edit
# PaymentController.edit(2,4, "in person", "description", "fries")

# Remove
#PaymentController.remove(payment_id)

# Find all
# _, all_payments = PaymentController.find_all()
# for payment in all_payments:
#     print(f"ID: {payment.id}, Amount: {payment.amount}, Payment Type: {payment.payment_type}")
#
#find by id
# _, payment = PaymentController.find_by_id(1)
# if payment:
#     print(f"Found Payment: Amount: {Payment.amount}, Payment Type: {Payment.payment_type}")

#find by payment type
# _, payment = PaymentController.find_by_payment_type("online")
# if payment:
#     print(f"Found Payment: ID: {Payment.id}, Amount: {Payment.amount}, Payment Type: {Payment.payment_type}")

#find by amount
# _, payment = PaymentController.find_by_amount(1)
# if payment:
#     print(f"Found Payment: ID: {Payment.id}, Amount: {Payment.amount}, Payment Type: {Payment.payment_type}")

#find by order
# _, payment = PaymentController.find_by_order("stuff")
# if payment:
#     print(f"Found Payment: ID: {Payment.id}, Amount: {Payment.amount}, Payment Type: {Payment.payment_type}")

PaymentView()