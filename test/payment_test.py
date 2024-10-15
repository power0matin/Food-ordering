from controller.payment_controller import PaymentController

# Save
PaymentController.save()

payment_id = 1

# Edit
PaymentController.edit(payment_id, )

# Remove
PaymentController.remove(payment_id)

# Find all
all_payments = PaymentController.find_all()
for payment in all_payments[1]:
    print(f"ID: {payment.id}, Amount: {payment.amount}, Payment Type: {payment.payment_type}")

# Find by ID
payment = PaymentController.find_by_id(payment_id)
print(f"Found Payment: Amount: {payment[1].amount}, Payment Type: {payment[1].payment_type}")
