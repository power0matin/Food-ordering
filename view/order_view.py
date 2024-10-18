from tkinter import *
import tkinter.messagebox as msg
from controller.order_controller import OrderController
from view.component import LabelWithEntry, Table


class OrderView:
    def reset_form(self):
        self.id.set(0)
        self.amount.set("")
        self.discount.set("")
        self.pure_amount.set("")

    def table_click(self, selected_item):
        print(selected_item)

    def save_click(self):
        status, message = OrderController.save(
            self.id.set(0),
            self.amount.set(""),
            self.discount.set(""),
            self.pure_amount.set("")
        )
        if status:
            msg.showinfo("Saved!", message)
            self.reset_form()
        else:
            msg.showerror("Error: NOT Saved!", message)

    def edit_click(self):
        status, message = OrderController.edit(
            self.id.get(),
            self.amount.get(),
            self.discount.get(),
            self.pure_amount.set("")
        )
        if status:
            msg.showinfo("Edited!", message)
            self.reset_form()
        else:
            msg.showerror("Error: NOT Edited!", message)

    def remove_click(self):
        if msg.askyesno("Remove Order", "Are you sure?"):
            status, message = OrderController.remove(self.id.get())
            if status:
                msg.showinfo("Removed!", message)
                self.reset_form()
            else:
                msg.showerror("Error: NOT Removed!", message)

    def find_all_click(self):
        if msg.askyesno("Find All Orders"):
            status, message = OrderController.find_all()
            if status:
                msg.showinfo("Found ALL!", message)
                self.reset_form()
            else:
                msg.showerror("Error: NOT Found!", message)

    def find_by_id_click(self):
        if msg.askyesno("Find By Id"):
            status, message = OrderController.find_by_id(self.id.get())
            if status:
                msg.showinfo("Found!", message)
                self.reset_form()
            else:
                msg.showerror("Error: NOT Found!", message)

    def __init__(self):
        win = Tk()
        win.title("Order View")
        win.resizable(False, False)
        win.geometry("900x400")

        self.id = LabelWithEntry(win, "Id", 30, 20, data_type="int", state="readonly")
        self.amount = LabelWithEntry(win, "Amount", 30, 60)
        self.discount = LabelWithEntry(win, "Discount", 30, 100)
        self.pure_amount = LabelWithEntry(win, "Pure Amount", 30, 140)

        self.table = Table(win,
                           ["Id", "Pure Amount", "Discount", "Amount"],
                           [30, 100, 50, 100],
                           250,
                           20,
                           self.table_click
                           )
        self.table.refresh_table(OrderController.find_all()[1])

        Button(win, text="Save", width=10, command=self.save_click).place(x=300, y=260)
        Button(win, text="Edit", width=10, command=self.edit_click).place(x=400, y=260)
        Button(win, text="Remove", width=10, command=self.remove_click).place(x=500, y=260)
        Button(win, text="Find By Id", width=10, command=self.find_by_id_click).place(x=600, y=260)
        Button(win, text="Find All", width=10, command=self.find_all_click).place(x=700, y=260)
        self.reset_form()

        win.mainloop()
