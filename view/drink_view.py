from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg

from controller.drink_controller import DrinkController
from view.component import LabelWithEntry, Table


class DrinkView:
    def reset_form(self):
        self.id.set(0)
        self.title.set("")
        self.price.set(0.0)
        self.duration.set(0)
        self.size.set("")
        self.available.set(True)

    def table_click(self, selected_item):
        self.id.set(selected_item['values'][0])
        self.title.set(selected_item['values'][1])
        self.price.set(selected_item['values'][2])
        self.duration.set(selected_item['values'][3])
        self.size.set(selected_item['values'][4])
        self.available.set(selected_item['values'][5])

    def save_click(self):
        try:
            drink = DrinkController.save(
                self.title.get(),
                self.price.get(),
                self.duration.get(),
                self.size.get(),
                self.available.get()
            )
            if drink:
                msg.showinfo("Save", "Drink saved successfully.")
                self.reset_form()
            else:
                msg.showerror("Save Error", "Failed to save drink.")
        except Exception as e:
            msg.showerror("Save Error", str(e))

    def edit_click(self):
        try:
            drink = DrinkController.edit(
                self.id.get(),
                self.title.get(),
                self.price.get(),
                self.duration.get(),
                self.size.get(),
                self.available.get()
            )
            if drink:
                msg.showinfo("Edit", "Drink updated successfully.")
                self.reset_form()
            else:
                msg.showerror("Edit Error", "Failed to update drink.")
        except Exception as e:
            msg.showerror("Edit Error", str(e))

    def remove_click(self):
        if msg.askyesno("Remove Drink", "Are you sure you want to remove this drink?"):
            try:
                drink = DrinkController.remove(self.id.get())
                if drink:
                    msg.showinfo("Remove", "Drink removed successfully.")
                    self.reset_form()
                else:
                    msg.showerror("Remove Error", "Drink not found or failed to remove.")
            except Exception as e:
                msg.showerror("Remove Error", str(e))

    def __init__(self):
        win = Tk()
        win.geometry("800x400")
        win.title("Drink Management")

        self.id = LabelWithEntry(win, "Id", 20, 20, data_type="int", state="readonly")
        self.title = LabelWithEntry(win, "Title", 20, 60)
        self.price = LabelWithEntry(win, "Price", 20, 100, data_type="float")
        self.duration = LabelWithEntry(win, "Duration", 20, 140, data_type="int")
        self.size = LabelWithEntry(win, "Size", 20, 180)
        self.available = LabelWithEntry(win, "Available (True/False)", 20, 220, data_type="bool")

        self.table = Table(win, ["Id", "Title", "Price", "Duration", "Size", "Available"],
                           [60, 100, 100, 80, 80, 60], 250, 20, self.table_click)
        self.table.refresh_table(DrinkController.find_all())

        Button(win, text="Save", width=10, command=self.save_click).place(x=100, y=300)
        Button(win, text="Edit", width=10, command=self.edit_click).place(x=100, y=330)
        Button(win, text="Remove", width=10, command=self.remove_click).place(x=100, y=360)

        self.reset_form()

        win.mainloop()