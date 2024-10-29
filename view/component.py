from tkinter import *
import tkinter.ttk as ttk


class LabelWithEntry:
    def __init__(self, window, text, x, y, data_type="str", distance=60, state="normal"):
        Label(window, text=text).place(x=x, y=y)
        match data_type:
            case "str":
                self.variable = StringVar()
            case "int":
                self.variable = IntVar()
            case "float":
                self.variable = DoubleVar()
            case "bool":
                self.variable = BooleanVar()
            case _:
                self.variable = StringVar()

        Entry(window, textvariable=self.variable, state=state).place(x=x + distance, y=y)

    def get(self):
        return self.variable.get()

    def set(self, value):
        self.variable.set(value)


class Table:
    def __init__(self, master, headers, widths, x, y, select_function=None):
        self.master = master
        self.x = x
        self.y = y
        self.headers = headers
        self.widths = widths
        self.select_function = select_function
        self.columns = list(range(len(headers)))

        self.table = ttk.Treeview(self.master, columns=self.columns, show="headings")
        for col in self.columns:
            self.table.column(col, width=self.widths[col])
            self.table.heading(col, text=self.headers[col])

        if select_function:
            self.table.bind("<ButtonRelease>", self.select_table)
            self.table.bind("<KeyRelease>", self.select_table)
        self.table.place(x=x, y=y)

    def refresh_table(self, data):
        self.table.delete(*self.table.get_children())

        for item in data:
            if hasattr(item, 'to_tuple'):
                values = item.to_tuple()
            else:
                values = item
            self.table.insert("", "end", values=values)

    def select_table(self, event):
        data = self.table.item(self.table.focus())["values"]
        if data:
            self.select_function(data)
