from tkinter import *
import tkinter.messagebox as msg
from controller import AdminController
from model.entity import Admin
from view.component import LabelWithEntry, Table


class AdminView:
    def reset_form(self):
        self.id.set(0)
        self.name.set("")
        self.family.set("")
        self.username.set("")
        self.password.set("")
        self.access_level.set(0)
        status, data = AdminController.find_all()
        if status:
            self.table.refresh_table(data)
        else:
            msg.showerror("Error", data)

    def table_click(self, selected_item):
        admin = AdminController.find_by_id(selected_item[0])
        self.id.set(admin.id)
        self.name.set(admin.name)
        self.family.set(admin.family)
        self.username.set(admin.username)
        self.password.set(admin.password)
        self.access_level.set(admin.access_level)

    def save_click(self):
        try:
            status, message = AdminController.save(
                self.name.get(),
                self.family.get(),
                self.username.get(),
                self.password.get(),
                self.access_level.get()
            )
            if status:
                msg.showinfo("Saved Successfully", message)
                self.reset_form()
            else:
                msg.showerror("Failed to Save", message)
        except Exception as e:
            msg.showerror("Failed to Save", str(e))

    def edit_click(self):
        try:
            status, message = AdminController.edit(
                self.id.get(),
                self.name.get(),
                self.family.get(),
                self.username.get(),
                self.password.get(),
                self.access_level.get()
            )
            if status:
                msg.showinfo("Edited Successfully", message)
                self.reset_form()
            else:
                msg.showerror("Failed to Edit", message)
        except Exception as e:
            msg.showerror("Failed to Edit", str(e))

    def remove_click(self):
        if msg.askyesno("Remove", "Are you sure?"):
            try:
                status, message = AdminController.remove(self.id.get())
                if status:
                    msg.showinfo("Removed Successfully", message)
                    self.reset_form()
                else:
                    msg.showerror("Failed to Remove", message)
            except Exception as e:
                msg.showerror("Failed to Remove", str(e))

    def find_all_click(self):
        try:
            admins = AdminController.find_all()
            self.table.refresh_table(admins)
            msg.showinfo("Find All Successfully", admins)
        except Exception as e:
            msg.showerror("Failed to Find", str(e))

    def find_by_username_click(self):
        user = self.username.get()
        try:
            admin = AdminController.find_by_username(user)
            if admin:
                self.table.refresh_table(admin)
                msg.showinfo("Find By Username", admin)
            else:
                msg.showerror("Failed to Find By Username", user)
        except Exception as e:
            msg.showerror("Failed to Find", str(e))

    def find_by_username_password(self):
        user = self.username.get()
        password = self.password.get()
        try:
            admin = AdminController.find_by_username(user, password)
            if admin:
                self.table.refresh_table(admin)
                msg.showinfo("Find By Username", admin)
            else:
                msg.showerror("Failed to Find By Username", user)
        except Exception as e:
            msg.showerror("Failed to Find", str(e))

    def find_by_access_level_click(self):
        try:
            access_level = self.access_level.get()
            admins = AdminController.find_by_access_level(access_level)
            if admins:
                self.table.refresh_table(admins)
                msg.showinfo("Find By Access Level", admins)
            else:
                msg.showerror("Failed to Find By Access Level", access_level)
        except Exception as e:
            msg.showerror("Failed to Find", str(e))

    def __init__(self):
        win = Tk()
        win.title("Admin View")
        win.resizable(False, False)
        win.geometry("900x450")

        self.id = LabelWithEntry(win, "Id", 25, 20, data_type="int", state="readonly")
        self.name = LabelWithEntry(win, "Name", 25, 60)
        self.family = LabelWithEntry(win, "Family", 25, 100)
        self.username = LabelWithEntry(win, "Username", 25, 140)
        self.password = LabelWithEntry(win, "Password", 25, 180)
        self.access_level = LabelWithEntry(win, "Access Level", 25, 220)

        self.table = Table(win, ["Id", "Name", "Family", "Username", "Password", "Access Level"],
                           [50, 100, 100, 100, 100, 100], 300, 20, self.table_click)

        Button(win, text="Save", width=15, command=self.save_click).place(x=100, y=280)
        Button(win, text="Edit", width=15, command=self.edit_click).place(x=100, y=320)
        Button(win, text="Remove", width=15, command=self.remove_click).place(x=100, y=360)
        Button(win, text="Find All", width=15, command=self.find_all_click).place(x=230, y=280)
        Button(win, text="Find By Username", width=20, command=self.find_by_username_click).place(x=230, y=320)
        Button(win, text="Find By Username & Password", width=25, command=self.find_by_username_password).place(x=230,
                                                                                                                y=360)
        Button(win, text="Find By Access Level", width=20, command=self.find_by_access_level_click).place(x=230, y=400)

        self.reset_form()
        win.mainloop()
