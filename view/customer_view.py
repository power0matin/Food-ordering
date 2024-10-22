from tkinter import *
import tkinter.messagebox as msg
from controller import CustomerController
from model.entity import admin, Customer
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
        status, data = CustomerController.find_all()
        if status:
            self.table.refresh_table(data)
        else:
            msg.showerror("Error", data)

    def table_click(self, selected_item):
        _, customer = CustomerController.find_by_id(selected_item[0])
        self.id.set(customer.id)
        self.name.set(customer.name)
        self.family.set(customer.family)
        self.email.set(customer.email)
        self.phone.set(customer.phone)
        self.username.set(customer.username)
        self.password.set(customer.password)

    def save_click(self):
        try:
            status, message = CustomerController.save(
                self.name.get(),
                self.family.get(),
                self.email.get(),
                self.phone.get(),
                self.username.get(),
                self.password.get()
            )
            if status:
                msg.showinfo("Saved!", message)
                self.reset_form()
            else:
                msg.showerror("Error: Couldn't Save!", message)
        except Exception as e:
            msg.showerror("Error: Couldn't Save!", str(e))

    def edit_click(self):
        try:
            status, message = CustomerController.edit(
                self.name.get(),
                self.family.get(),
                self.email.get(),
                self.phone.get(),
                self.username.get(),
                self.password.get()
            )
            if status:
                msg.showinfo("Edited!", message)
                self.reset_form()
            else:
                msg.showerror("Error: Couldn't Edit!", message)
        except Exception as e:
            msg.showerror("Error: Couldn't Edit!", str(e))

    def remove_click(self):
        if msg.askyesno("Remove Customer", "Are you sure?"):
            try:
                status, message = CustomerController.remove(self.id.get())
                if status:
                    msg.showinfo("Removed!", message)
                    self.reset_form()
                else:
                    msg.showerror("Error: Couldn't Remove!", message)
            except Exception as e:
                msg.showerror("Error: Couldn't Remove!", str(e))

    def find_all_click(self):
        try:
            customers = CustomerController.find_all()
            self.table.refresh_table(customers)
            msg.showinfo("Found All!", customers)
        except Exception as e:
            msg.showerror("Error: NOT Found!", str(e))

    def find_by_id_click(self):
        id = self.id.get()
        try:
            customer = CustomerController.find_by_id(id)
            if customer:
                self.table.refresh_table(admin)
                msg.showinfo("Found By ID!", customer)
            else:
                msg.showerror("Error: Couldn't Find By ID!", id)
        except Exception as e:
            msg.showerror("Error: Couldn't Find By ID!", str(e))

    def find_by_username_click(self):
        user = self.username.get()
        try:
            customer = CustomerController.find_by_username(user)
            if customer:
                self.table.refresh_table(customer)
                msg.showinfo("Found By Username!", customer)
            else:
                msg.showerror("Error: Couldn't Find By Username!", user)
        except Exception as e:
            msg.showerror("Error: Couldn't Find By Username!", str(e))

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
        win.geometry("900x400")

        # entry view:
        self.id = LabelWithEntry(win, "Id", 30, 20, data_type="int", state="readonly")
        self.name = LabelWithEntry(win, "Name", 30, 60)
        self.family = LabelWithEntry(win, "Family", 30, 100)
        self.email = LabelWithEntry(win, "Email", 30, 140)
        self.phone = LabelWithEntry(win, "Phone", 30, 180)
        self.username = LabelWithEntry(win, "Username", 30, 220)
        self.password = LabelWithEntry(win, "Password", 30, 260)

        # table columns view:
        self.table = Table(win,
                           ["Id", "Name", "Family", "Email", "Phone", "Username", "Password"],
                           [30, 70, 70, 135, 100, 70, 100],
                           250,
                           20,
                           self.table_click
                           )

        # buttons view:
        Button(win, text="Save", width=10, command=self.save_click).place(x=300, y=260)
        Button(win, text="Edit", width=10, command=self.edit_click).place(x=400, y=260)
        Button(win, text="Remove", width=10, command=self.remove_click).place(x=500, y=260)
        Button(win, text="Find By Id", width=10, command=self.find_by_id_click).place(x=600, y=260)
        Button(win, text="Find All", width=10, command=self.find_all_click).place(x=700, y=260)
        Button(win, text="Find By Username", width=15, command=self.find_by_username_click).place(x=350, y=320)
        Button(win, text="Find By Username & Password", width=30,
               command=self.find_by_username_and_password_click).place(x=520, y=320)

        self.reset_form()

        win.mainloop()
