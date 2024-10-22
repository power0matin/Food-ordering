from tkinter import *
import tkinter.messagebox as msg
from controller.food_controller import FoodController
from model.entity import Food
from view.component import LabelWithEntry, Table


class FoodView:
    def reset_form(self):
        self.id.set(0)
        self.title.set("")
        self.description.set("")
        self.price.set(0.0)
        self.duration.set(0)
        self.size.set("")
        self.available.set(True)
        status, data = FoodController.find_all()
        if status:
            self.table.refresh_table(data)
        else:
            msg.showerror("Error", data)

    def table_click(self, selected_item):
        _, food = FoodController.find_by_id(selected_item[0])
        self.id.set(food.id)
        self.title.set(food.title)
        self.description.set(food.description)
        self.price.set(food.price)
        self.duration.set(food.duration)
        self.size.set(food.size)
        self.available.set(food.available)

    def save_click(self):
        try:
            status, message = FoodController.save(
                self.title.get(),
                self.description.get(),
                self.price.get(),
                self.duration.get(),
                self.size.get(),
                self.available.get()
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
            status, message = FoodController.edit(
                self.id.get(),
                self.title.get(),
                self.description.get(),
                self.price.get(),
                self.duration.get(),
                self.size.get(),
                self.available.get()
            )
            if status:
                msg.showinfo("Edited Successfully", message)
                self.reset_form()
            else:
                msg.showerror("Failed to Edit", message)
        except Exception as e:
            msg.showerror("Failed to Edit", str(e))

    def remove_click(self):
        if msg.askyesno("Remove Food", "Are you sure you want to remove this food?"):
            try:
                status, message = FoodController.remove(self.id.get())
                if status:
                    msg.showinfo("Removed Successfully", message)
                    self.reset_form()
                else:
                    msg.showerror("Failed to Remove", message)
            except Exception as e:
                msg.showerror("Failed to Remove", str(e))

    def __init__(self):
        win = Tk()
        win.geometry("800x400")
        win.title("Food Management")

        self.id = LabelWithEntry(win, "Id", 20, 20, data_type="int", state="readonly")
        self.title = LabelWithEntry(win, "Title", 20, 60)
        self.description = LabelWithEntry(win, "Description", 20, 100)
        self.price = LabelWithEntry(win, "Price", 20, 140, data_type="float")
        self.duration = LabelWithEntry(win, "Duration", 20, 180, data_type="int")
        self.size = LabelWithEntry(win, "Size", 20, 220)
        self.available = LabelWithEntry(win, "Available (True/False)", 20, 260, data_type="bool")

        self.table = Table(win, ["Id", "Title", "Description", "Price", "Duration", "Size", "Available"],
                           [60, 100, 150, 100, 80, 80, 60], 250, 20, self.table_click)

        Button(win, text="Save", width=10, command=self.save_click).place(x=100, y=300)
        Button(win, text="Edit", width=10, command=self.edit_click).place(x=100, y=330)
        Button(win, text="Remove", width=10, command=self.remove_click).place(x=100, y=360)

        self.reset_form()

        win.mainloop()
