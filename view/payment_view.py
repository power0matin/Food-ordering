from tkinter import *
import tkinter.messagebox as msg
from controller.payment_controller import PaymentController
from view.component import LabelWithEntry, Table


class PaymentView:
    def reset_form(self):
        self.id.set(0)
        self.name.set("")
        self.family.set("")
        self.amount.set(0)
        self.payment_type.set("")
        self.description.set("")
        self.order.set("")

    def table_click(self, selected_item):
        print(selected_item)

    def save_click(self):
        status, message = PaymentController.save(
            self.name.get(),
            self.family.get(),
            self.amount.set(0),
            self.payment_type.set(""),
            self.description.set(""),
            self.order.set("")
        )
        if status:
            msg.showinfo("Saved!", message)
            self.reset_form()
        else:
            msg.showerror("Error: NOT Saved!", message)

    def edit_click(self):
        status, message = PaymentController.edit(
            self.id.get(),
            self.name.get(),
            self.family.get(),
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

    def remove_click(self):
        if msg.askyesno("Remove Payment", "Are you sure?"):
            status, message = PaymentController.remove(self.id.get())
            if status:
                msg.showinfo("Removed!", message)
                self.reset_form()
            else:
                msg.showerror("Error: NOT Removed!", message)

    def find_all_click(self):
        if msg.askyesno("Find All Payments"):
            status, message = PaymentController.find_all()
            if status:
                msg.showinfo("Found ALL!", message)
                self.reset_form()
            else:
                msg.showerror("Error: NOT Found!", message)

    def find_by_id_click(self):
        if msg.askyesno("Find By Id"):
            status, message = PaymentController.find_by_id(self.id.get())
            if status:
                msg.showinfo("Found!", message)
                self.reset_form()
            else:
                msg.showerror("Error: NOT Found!", message)

    def find_by_payment_type_click(self):
        if msg.askyesno("Find By Payment Type"):
            status, message = PaymentController.find_by_payment_type(self.payment_type.get())
            if status:
                msg.showinfo("Found!", message)
                self.reset_form()
            else:
                msg.showerror("Error: NOT Found!", message)

    def find_by_amount_click(self):
        if msg.askyesno("Find By Amount"):
            status, message = PaymentController.find_by_amount(self.amount.get())
            if status:
                msg.showinfo("Found!", message)
                self.reset_form()
            else:
                msg.showerror("Error: NOT Found!", message)

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
        win.geometry("900x400")

        self.id = LabelWithEntry(win, "Id", 30, 20, data_type="int", state="readonly")
        self.name = LabelWithEntry(win, "Name", 30, 60)
        self.family = LabelWithEntry(win, "Family", 30, 100)
        self.amount = LabelWithEntry(win, "Amount", 30, 140)
        self.payment_type = LabelWithEntry(win, "Payment Type", 30, 180)
        self.description = LabelWithEntry(win, "Description", 30, 220)
        self.order = LabelWithEntry(win, "Order", 30, 260)

        self.table = Table(win,
                           ["Id", "Name", "Family", "Amount", "Payment Type", "Description", "Order"],
                           [30, 70, 70, 60, 100, 150, 150],
                           250,
                           20,
                           self.table_click
                           )
        self.table.refresh_table(PaymentController.find_all()[1])

        Button(win, text="Save", width=10, command=self.save_click).place(x=300, y=260)
        Button(win, text="Edit", width=10, command=self.edit_click).place(x=400, y=260)
        Button(win, text="Remove", width=10, command=self.remove_click).place(x=500, y=260)
        Button(win, text="Find By Id", width=10, command=self.find_by_id_click).place(x=600, y=260)
        Button(win, text="Find All", width=10, command=self.find_all_click).place(x=700, y=260)
        Button(win, text="Find By Payment Type", width=25, command=self.find_by_payment_type_click).place(x=300, y=320)
        Button(win, text="Find By Amount", width=15, command=self.find_by_amount_click).place(x=500, y=320)
        Button(win, text="Find By Order", width=15, command=self.find_by_order_click).place(x=6500, y=320)
        self.reset_form()

        win.mainloop()