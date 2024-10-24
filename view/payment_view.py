from tkinter import *
import tkinter.messagebox as msg
from tkinter.ttk import Combobox

from controller.payment_controller import PaymentController
from view.component import LabelWithEntry, Table


class PaymentView:

    # reset forms:
    def reset_form(self):
        self.id.set(0)
        self.amount.set(0)
        self.payment_type.set("")
        self.description.set("")
        self.order.set("")
        status, data = PaymentController.find_all()
        if status:
            self.table.refresh_table(data)
        else:
            msg.showerror("Error", data)

    # table function:
    def table_click(self, selected_item):
        payment = PaymentController.find_by_id(selected_item[0])
        self.id.set(payment.id)
        self.amount.set(payment.amount)
        self.payment_type.set(payment.payment_type)
        self.description.set(payment.description)
        self.order.set(payment.order)

    #     todo : complete it ...

    # save function:
    def save_click(self):
        try:
            status, message = PaymentController.save(
                self.amount.get(),
                self.payment_type.get(),
                self.description.get(),
                self.order.get()
            )
            if status:
                msg.showinfo("Saved!", message)
                self.reset_form()
            else:
                msg.showerror("Error: Couldn't Save!", message)
        except Exception as e:
            msg.showerror("Error: Couldn't Save!", str(e))

    # edit function:
    def edit_click(self):
        try:
            status, message = PaymentController.edit(
                self.id.get(),
                self.amount.get(),
                self.payment_type.get(),
                self.description.get(),
                self.order.get()
            )
            if status:
                msg.showinfo("Edited!", message)
                self.reset_form()
            else:
                msg.showerror("Error: Couldn't Edit!", message)
        except Exception as e:
            msg.showerror("Error: Couldn't Edit!", str(e))

    # remove function:
    def remove_click(self):
        try:
            if msg.askyesno("Remove Payment", "Are you sure?"):
                status, message = PaymentController.remove(self.id.get())
                if status:
                    msg.showinfo("Removed!", message)
                    self.reset_form()
                else:
                    msg.showerror("Error: Couldn't Remove!", message)
        except Exception as e:
            msg.showerror("Error: Couldn't Remove!", str(e))

    # find all function:
    def find_all_click(self):
        if msg.askyesno("Find All Payments"):
            status, message = PaymentController.find_all()
            if status:
                msg.showinfo("Found ALL!", message)
                self.reset_form()
            else:
                msg.showerror("Error: NOT Found!", message)

    # find by id function:
    def find_by_id_click(self):
        if msg.askyesno("Find By Id"):
            status, message = PaymentController.find_by_id(self.id.get())
            if status:
                msg.showinfo("Found!", message)
                self.reset_form()
            else:
                msg.showerror("Error: NOT Found!", message)

    # find by payment type function:
    def find_by_payment_type_click(self):
        if msg.askyesno("Find By Payment Type"):
            status, message = PaymentController.find_by_payment_type(self.payment_type.get())
            if status:
                msg.showinfo("Found!", message)
                self.reset_form()
            else:
                msg.showerror("Error: NOT Found!", message)

    # find by amount function:
    def find_by_amount_click(self):
        if msg.askyesno("Find By Amount"):
            status, message = PaymentController.find_by_amount(self.amount.get())
            if status:
                msg.showinfo("Found!", message)
                self.reset_form()
            else:
                msg.showerror("Error: NOT Found!", message)

    # find by order function:
    def find_by_order_click(self):
        if msg.askyesno("Find By Order"):
            status, message = PaymentController.find_by_order(self.order.get())
            if status:
                msg.showinfo("Found!", message)
                self.reset_form()
            else:
                msg.showerror("Error: NOT Found!", message)

    def __init__(self):
        win = Tk()
        win.title("Payment View")
        win.resizable(False, False)
        win.geometry("850x360")

        # entry view:
        self.id = LabelWithEntry(win, "Id", 30, 40, data_type="int", state="readonly")
        self.amount = LabelWithEntry(win, "Amount", 30, 80)
        # self.payment_type.setAccessibleName("Payment Type:")
        self.payment_type = Combobox(win, values=["Online", "In Person"], name="payment type:", state="readonly")
        self.payment_type.place(x=80, y=120)
        self.description = LabelWithEntry(win, "Description", 30, 160)
        self.order = LabelWithEntry(win, "Order", 30, 200)

        # table columns view:
        self.table = Table(win,
                           ["Id", "Amount", "Date", "Payment Type", "Description", "Order"],
                           [30, 70, 130, 100, 150, 70],
                           250,
                           20,
                           self.table_click
                           )
        self.table.refresh_table(PaymentController.find_all()[1])

        # buttons view:
        Button(win, text="Save", width=10, command=self.save_click).place(x=280, y=260)
        Button(win, text="Edit", width=10, command=self.edit_click).place(x=390, y=260)
        Button(win, text="Remove", width=10, command=self.remove_click).place(x=500, y=260)
        Button(win, text="Find By Id", width=10, command=self.find_by_id_click).place(x=610, y=260)
        Button(win, text="Find All", width=10, command=self.find_all_click).place(x=720, y=260)
        Button(win, text="Find By Payment Type", width=25, command=self.find_by_payment_type_click).place(x=310, y=310)
        Button(win, text="Find By Amount", width=15, command=self.find_by_amount_click).place(x=520, y=310)
        Button(win, text="Find By Order", width=15, command=self.find_by_order_click).place(x=660, y=310)
        self.reset_form()

        win.mainloop()
