from tkinter import *
import tkinter.messagebox as msg
from controller.admin_controller import AdminController
from view.component import LabelWithEntry, Table


class AdminView:
    def reset_form(self):
        self.id.set(0)
        self.name.set("")
        self.family.set("")
        self.username.set("")
        self.password.set("")
        self.access_level.set(0)
        self.refresh_table()

    def table_click(self, selected_item):
        print(selected_item)

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
            msg.showerror("Failed to Save", e)

    def edit_click(self):
        try:
            status, message = AdminController.edit(
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
            msg.showerror("Failed to Edit", e)

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
                msg.showerror("Failed to Remove", e)

    def find_all_click(self):
        try:
            admins = AdminController.find_all()
            self.table.refresh_table(admins)
            msg.showinfo("Find All Successfully", admins)
        except Exception as e:
            msg.showerror("Failed to Find", e)

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
            msg.showerror("Failed to Find", e)

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
            msg.showerror("Failed to Find", e)

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
            msg.showerror("Failed to Find", e)

    def __init__(self):
        win = Tk()
        win.title("Admin View")
        win.resizable(False, False)
        win.geometry("650x450")

        self.id = LabelWithEntry(win, "Id", 20, 20, data_type="int", state="readonly")
        self.name = LabelWithEntry(win, "Name", 20, 60, data_type="text")
        self.family = LabelWithEntry(win, "Family", 20, 100, data_type="text")
        self.username = LabelWithEntry(win, "Username", 20, 100, data_type="text")
        self.password = LabelWithEntry(win, "Password", 20, 100, data_type="text")
        self.access_level = LabelWithEntry(win, "Access Level", 20, 100, data_type="int")

        self.table = Table(win, ["Id", "Name", "Family", "Username", "Password", "Access Level"],
                           [60, 100, 100, 100, 100, 100], 250, 20, self.table_click)
        self.table.refresh_table(AdminController.find_all())

        Button(win, text="Save", width=10, command=self.save_click).place(x=100, y=260)
        Button(win, text="Edit", width=10, command=self.edit_click).place(x=100, y=290)
        Button(win, text="Remove", width=10, command=self.remove_click).place(x=100, y=320)
        Button(win, text="Find All", width=10, command=self.find_all_click).place(x=200, y=260)
        Button(win, text="Find By Username", width=15, command=self.find_by_username_click).place(x=200, y=290)
        Button(win, text="Find By Username & Password", width=20, command=self.find_by_username_password).place(x=200,
                                                                                                                y=320)
        Button(win, text="Find By Access Level", width=15, command=self.find_by_access_level_click).place(x=200, y=350)

        self.reset_form()

        win.mainloop()
