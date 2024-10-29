from tkinter import *

import tkinter.messagebox as msg

from controller.table_controller import TableController
from view.component import LabelWithEntry, Table

class TableView:
    def reset_form(self):
        self.id.set(0)
        self.title.set("")
        self.location.set("")
        self.number.set(0)
        self.is_empty.set(True)
        status, data = TableController.find_all()
        if status:
            self.table.refresh_table(data)
        else:
            msg.showerror("Error", data)

    def table_click(self, selected_item):
        _, table = TableController.find_by_id(selected_item[0])
        self.id.set(table.id)
        self.title.set(table.title)
        self.location.set(table.location)
        self.number.set(table.number)
        self.is_empty.set(table.is_empty)

    def save_click(self):
        try:
            status, message = TableController.save(
                self.title.get(),
                self.location.get(),
                self.number.get(),
                self.is_empty.get()
            )
            if status:
                msg.showinfo("Saved Successfully", message)
                self.reset_form()
            else:
                msg.showerror("Failed to Save", message)
        except Exception as e:
            msg.showerror("Failed to Save", f"{e}")

    def edit_click(self):
        try:
            status, message = TableController.edit(
                self.id.get(),
                self.title.get(),
                self.location.get(),
                self.number.get(),
                self.is_empty.get()
            )
            if status:
                msg.showinfo("Edited Successfully", message)
                self.reset_form()
            else:
                msg.showerror("Failed to Edit", message)
        except Exception as e:
            msg.showerror("Failed to Edit", f"{e}")

    def remove_click(self):
        if msg.askyesno("Remove", "Are you sure?"):
            try:
                status, message = TableController.remove(self.id.get())
                if status:
                    msg.showinfo("Removed Successfully", message)
                    self.reset_form()
                else:
                    msg.showerror("Failed to Remove", message)
            except Exception as e:
                msg.showerror("Failed to Remove", f"{e}")

    def find_all_click(self):
        try:
            tables = TableController.find_all()
            self.table.refresh_table(tables)
            msg.showinfo("Find All Successfully", tables)
        except Exception as e:
            msg.showerror("Failed to Find", f"{e}")

    def find_empty_table_click(self):
        is_empty = self.is_empty.get()
        try:
            table = TableController.find_empty_tables(is_empty)
            if table:
                self.table.refresh_table(table)
                msg.showinfo("Find Empty Table", table)
            else:
                msg.showerror("Failed to empty table", is_empty)
        except Exception as e:
            msg.showerror("Failed to Find", f"{e}")

    def find_by_number_click(self):
        number = self.number.get()
        try:
            table = TableController.find_by_number(number)
            if table:
                self.table.refresh_table(table)
                msg.showinfo("Find By Number", table)
            else:
                msg.showerror("Failed to Find By Number", number)
        except Exception as e:
            msg.showerror("Failed to Find", f"{e}")

    def __init__(self):
        win = Tk()
        win.title("Table View")
        win.resizable(False, False)
        win.geometry("730x380")

        self.id = LabelWithEntry(win, "Id", 20, 20, data_type="int")
        self.title = LabelWithEntry(win, "Title", 20, 60, data_type="text")
        self.location = LabelWithEntry(win, "Location", 20, 100, data_type="text")
        self.number = LabelWithEntry(win, "Number", 20, 140, data_type="int")
        self.is_empty = LabelWithEntry(win, "Is_Empty", 20, 180, data_type="bool")

        self.table = Table(win, ["Id", "title", "location", "number", "is_empty"],
                           [60, 100, 100, 100, 100, 100], 250, 20, self.table_click)

        Button(win, text="Save", width=10, command=self.save_click).place(x=100, y=260)
        Button(win, text="Edit", width=10, command=self.edit_click).place(x=100, y=290)
        Button(win, text="Remove", width=10, command=self.remove_click).place(x=100, y=320)
        Button(win, text="Find All", width=10, command=self.find_all_click).place(x=200, y=260)
        Button(win, text="Find By Number", width=15, command=self.find_by_number_click).place(x=200, y=290)
        Button(win, text="Find Empty Table", width=20, command=self.find_empty_table_click).place(x=200, y=320)

        self.reset_form()

        win.mainloop()