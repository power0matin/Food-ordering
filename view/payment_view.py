import tkinter
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

    # table function:
    def table_click(self, selected_item):
        print(selected_item)

    # save function:
    def save_click(self):
        status, message = PaymentController.save(
            self.amount.set(1),
            self.payment_type.set(""),
            self.description.set(""),
            self.order.set("")
        )
        if status:
            msg.showinfo("Saved!", message)
            self.reset_form()
        else:
            msg.showerror("Error: NOT Saved!", message)

    # edit function:
    def edit_click(self):
        status, message = PaymentController.edit(
            self.id.get(),
            self.amount.set(0),
            self.payment_type.set(""),
            self.description.set(""),
            self.order.set("")
        )
        if status:
            msg.showinfo("Edited!", message)
            self.reset_form()
        else:
            msg.showerror("Error: NOT Edited!", message)

    # remove function:
    def remove_click(self):
        if msg.askyesno("Remove Payment", "Are you sure?"):
            status, message = PaymentController.remove(self.id.get())
            if status:
                msg.showinfo("Removed!", message)
                self.reset_form()
            else:
                msg.showerror("Error: NOT Removed!", message)

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
        self.payment_type = Combobox(win,values=["Online","In Person"])
        self.payment_type.place(x=80,y=120)
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
