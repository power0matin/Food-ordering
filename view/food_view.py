from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg

from controller.food_controller import FoodController
from view.component import LabelWithEntry, Table


class FoodView:
    def reset_form(self):
        self.id.set(0)
        self.title.set("")
        self.price.set(0.0)
        self.duration.set(0)
        self.description.set("")
        self.size.set("")
        self.available.set(True)

    def table_click(self, selected_item):
        self.id.set(selected_item['values'][0])
        self.title.set(selected_item['values'][1])
        self.price.set(selected_item['values'][2])
        self.duration.set(selected_item['values'][3])
        self.description.set(selected_item['values'][4])
        self.size.set(selected_item['values'][5])
        self.available.set(selected_item['values'][6])

    def save_click(self):
        try:
            food = FoodController.save(self.title.get(), self.description.get(), self.price.get(), self.duration.get(),
                                       self.size.get(), self.available.get())
            if food:
                msg.showinfo("Save", "Food saved successfully.")
                self.reset_form()
            else:
                msg.showerror("Save Error", "Failed to save food.")
        except Exception as e:
            msg.showerror("Save Error", str(e))

    def edit_click(self):
        try:
            food = FoodController.edit(self.id.get(), self.title.get(), self.description.get(), self.price.get(),
                                       self.duration.get(), self.size.get(), self.available.get())
            if food:
                msg.showinfo("Edit", "Food updated successfully.")
                self.reset_form()
            else:
                msg.showerror("Edit Error", "Failed to update food.")
        except Exception as e:
            msg.showerror("Edit Error", str(e))

    def remove_click(self):
        if msg.askyesno("Remove Food", "Are you sure you want to remove this food?"):
            try:
                food = FoodController.remove(self.id.get())
                if food:
                    msg.showinfo("Remove", "Food removed successfully.")
                    self.reset_form()
                else:
                    msg.showerror("Remove Error", "Food not found or failed to remove.")
            except Exception as e:
                msg.showerror("Remove Error", str(e))

    def __init__(self):
        win = Tk()
        win.geometry("800x400")
        win.title("Food Management")

        self.id = LabelWithEntry(win, "Id", 20, 20, data_type="int", state="readonly")
        self.title = LabelWithEntry(win, "Title", 20, 60)
        self.price = LabelWithEntry(win, "Price", 20, 100, data_type="float")
        self.duration = LabelWithEntry(win, "Duration", 20, 140, data_type="int")
        self.description = LabelWithEntry(win, "Description", 20, 180)
        self.size = LabelWithEntry(win, "Size", 20, 220)
        self.available = LabelWithEntry(win, "Available (True/False)", 20, 260, data_type="bool")

        self.table = Table(win, ["Id", "Title", "Price", "Duration", "Description", "Size", "Available"],
                           [60, 100, 100, 80, 200, 80, 60], 250, 20, self.table_click)
        self.table.refresh_table(FoodController.find_all())

        Button(win, text="Save", width=10, command=self.save_click).place(x=100, y=300)
        Button(win, text="Edit", width=10, command=self.edit_click).place(x=100, y=330)
        Button(win, text="Remove", width=10, command=self.remove_click).place(x=100, y=360)

        self.reset_form()

        win.mainloop()
