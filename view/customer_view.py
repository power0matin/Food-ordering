#customer_view - Aida Shams
from tkinter import *
import tkinter.messagebox as msg
from controller.customer_controller import CustomerController
from view.component import LabelWithEntry, Table

class CustomerView:
    def reset_form(self):
        self.id.set(0)
        self.name.set("")
        self.family.set("")
        self.email.set("")
        self.phone.set("")
        self.username.set("")
        self.password.set("")

    def table_click(self, selected_item):
        print(selected_item)

    def save_click(self):
        status, message = CustomerController.save(self.name.get(), self.family.get(), self.email.set(), self.phone.set(),
                                                  self.username.set(), self.password.set())
        if status:
            msg.showinfo("Saved!", message)
            self.reset_form()
        else:
            msg.showerror("Error: NOT Saved!", message)

    def edit_click(self):
        status, message = CustomerController.edit(self.id.get(), self.name.get(), self.family.get(), self.email.set(),
                                                  self.phone.set(), self.username.set(), self.password.set())
        if status:
            msg.showinfo("Edited!", message)
            self.reset_form()
        else:
            msg.showerror("Error: NOT Edited!", message)

    def remove_click(self):
        if msg.askyesno("Remove Customer", "Are you sure?"):
            status, message = CustomerController.remove(self.id.get())
            if status:
                msg.showinfo("Removed!", message)
                self.reset_form()
            else:
                msg.showerror("Error: NOT Removed!", message)

    def find_all_click(self):
        if msg.askyesno("Find All Customers"):
            status, message = CustomerController.find_all()
            if status:
                msg.showinfo("Found ALL!", message)
                self.reset_form()
            else:
                msg.showerror("Error: NOT Found!", message)

    def find_by_id_click(self):
        if msg.askyesno("Find By Id"):
            status, message = CustomerController.find_by_id(self.id.get())
            if status:
                msg.showinfo("Found!", message)
                self.reset_form()
            else:
                msg.showerror("Error: NOT Found!", message)

    def find_by_username_click(self):
        if msg.askyesno("Find By Username"):
            status, message = CustomerController.find_by_username(self.username.get())
            if status:
                msg.showinfo("Found!", message)
                self.reset_form()
            else:
                msg.showerror("Error: NOT Found!", message)

    def find_by_username_and_password_click(self):
        if msg.askyesno("Find By Username & Password"):
            status, message = CustomerController.find_by_username_and_password(self.username.get(), self.password.get())
            if status:
                msg.showinfo("Found!", message)
                self.reset_form()
            else:
                msg.showerror("Error: NOT Found!", message)

    def __init__(self):
        win = Tk()
        win.title("Customer View")
        win.resizable(False, False)
        win.geometry("650x450")

        self.id = LabelWithEntry(win, "Id", 20, 20, data_type="int", state="readonly")
        self.name = LabelWithEntry(win, "Name", 20, 60)
        self.family = LabelWithEntry(win, "Family", 20, 100)
        self.email = LabelWithEntry(win, "Email", 20, 140)
        self.phone = LabelWithEntry(win, "Phone", 20, 140)
        self.username = LabelWithEntry(win, "Username", 20, 140)
        self.password = LabelWithEntry(win, "Password", 20, 140)

        self.table = Table(win, ["Id", "Name", "Family", "Email", "Phone", "Username", "Password"], [60,
                                                                                                     100, 100, 100, 100,
                                                                                                     100, 100], 250, 20, self.table_click)
        self.table.refresh_table(CustomerController.find_all()[1])

        Button(win, text="Save", width=10, command=self.save_click).place(x=100, y=180)
        Button(win, text="Edit", width=10, command=self.edit_click).place(x=100, y=210)
        Button(win, text="Remove", width=10, command=self.remove_click).place(x=100, y=240)
        Button(win, text="Find By Id", width=15, command=self.find_by_id_click).place(x=100, y=260)
        Button(win, text="Find All", width=10, command=self.find_all_click).place(x=200, y=260)
        Button(win, text="Find By Username", width=15, command=self.find_by_username_click).place(x=200, y=290)
        Button(win, text="Find By Username & Password", width=20, command=self.find_by_username_and_password_click).place(x=200,
                                                                                                                y=320)
#COULD NOT TEST!!!!!! sqlalchemy error again!
        self.reset_form()

        win.mainloop()