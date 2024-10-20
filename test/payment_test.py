from controller.payment_controller import PaymentController

# Save
# todo : error
# PaymentController.save()

payment_id = 1

# Edit
# todo : error
# PaymentController.edit(payment_id, )

# Remove
PaymentController.remove(payment_id)

# Find all
# all_payments = PaymentController.find_all()
# for payment in all_payments[1]:
#     print(f"ID: {payment.id}, Amount: {payment.amount}, Payment Type: {payment.payment_type}")

# todo : error
# Find by ID
all_payments = PaymentController.find_by_id(payment_id)
for Payment in all_payments[1]:
    print(f"Found Payment: Amount: {Payment[1].amount}, Payment Type: {Payment[1].payment_type}")
