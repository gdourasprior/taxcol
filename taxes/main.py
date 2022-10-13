import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename

import numpy as np
import pandas as pd

# -----/ Constants


# -----/ Pandas Stuff


# -----/ Save/Load Functions
def setup(title: str = "Taxes", geometry: str = "500x400") -> tk.Tk:
    window = tk.Tk()
    window.title(title)
    window.geometry(geometry)

    return window


def format_input(value):
    if not value:
        value = 0.0

    value = np.float64(value)

    if value < 0:
        value = 0

    return value


class Tax:
    def __init__(self):
        self._COLUMNS = ["Day", "Month", "Food", "Item", "Power", "Water", "Internet", "Fuel", "Rent"]

        self.window = None
        self.df = None
        self.location = None
        self.saved = False

    def load_from_file(self) -> None:
        filepath = askopenfilename(
            filetypes=[("CSV Files ", "*.csv")]
        )
        if not filepath:  # Create message saying failed, and return empty dataframe, with correct headers
            messagebox.showwarning(title="Failed to identify path", message="The specified filepath does not exist")
            self.df = pd.DataFrame(self._COLUMNS)
        self.df = pd.read_csv(filepath_or_buffer=filepath)

    def save_to_file(self) -> None:
        filepath = asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV Files", "*.csv")]
        )
        if not filepath:
            messagebox.showwarning(title="Failed to identify path", message="The specified filepath does not exist")
            self.saved = False

        self.df.to_csv(path_or_buf=filepath, index=False)
        self.saved = True

    # -----/ UI Support Functions

    def load(self, current: tk.Tk) -> None:
        self.load_from_file()
        self.entry(current=current)
        self.set_df_state()

    def save(self):
        self.save_to_file()

        if not self.saved:
            message = "File not saved!"
            messagebox.showinfo(title="Status", message=message)

    def set_df_state(self):
        self.df.astype(
            {
                "Day": str,
                "Month": str,
                "Food": 'float64',
                "Item": 'float64',
                "Power": 'float64',
                "Water": 'float64',
                "Internet": 'float64',
                "Fuel": 'float64',
                "Rent": 'float64'
            }
        )

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if key in ['Day', 'Month']:
                if not value:
                    messagebox.showwarning("Date MUST be SET completely!", "Set Day and Month!\nUpdate Aborted.")
                    break

        temp = pd.DataFrame([kwargs])
        self.df = pd.concat([self.df, temp])

    def tally_up(self):
        print("Tally Up Run!")

        cols = list()

        for col in self._COLUMNS:
            if col not in ['Day', 'Month']:
                cols.append(col)

        result = self.df[cols].sum()

        print(result.to_string())

    # -----/ UI Functions

    def init(self) -> None:
        window = setup("Start")

        frame = tk.Frame(master=window)

        exist_btn = tk.Button(
            master=frame,
            text="Existing CSV",
            command=lambda: self.load(current=window)
        )
        new_btn = tk.Button(
            master=frame,
            text="New CSV",
            command=lambda: self.entry(current=window)
        )

        exist_btn.grid(row=0, column=0)
        new_btn.grid(row=0, column=1)
        frame.pack()

        window.mainloop()

    def start(self, current: tk.Tk) -> None:
        current.destroy()
        self.init()

    def entry(self, current: tk.Tk) -> None:
        if self.df is None:
            messagebox.showinfo(title="Status", message="No DataFrame detected! Generating empty DataFrame")
            self.df = pd.DataFrame(columns=self._COLUMNS)
            self.set_df_state()

        window = setup("Entry Form", "500x485")
        current.destroy()

        tk.Label(master=window, text="Input the day and month").pack()

        frame_date = tk.Frame(master=window)

        lbl_day = tk.Label(master=frame_date, text="Select a Day")
        select_day = tk.Spinbox(master=frame_date, from_=1, to=31)
        lbl_month = tk.Label(master=frame_date, text="Select a Month")
        select_month = tk.Spinbox(master=frame_date, from_=1, to=12)

        lbl_day.grid(row=0, column=0)
        select_day.grid(row=0, column=1, padx=5)
        lbl_month.grid(row=0, column=2)
        select_month.grid(row=0, column=3, padx=5)

        frame_date.pack(padx=5, pady=10)

        frame_receipt = tk.Frame(master=window)

        tk.Label(master=window, text="Input Receipt Costs").pack()

        lbl_food = tk.Label(master=frame_receipt, text="Total Food Cost", width=15)
        entry_food = tk.Entry(master=frame_receipt)
        lbl_item = tk.Label(master=frame_receipt, text="Total Item Cost", width=15)
        entry_item = tk.Entry(master=frame_receipt)

        lbl_food.pack()
        entry_food.pack()
        lbl_item.pack()
        entry_item.pack()

        frame_receipt.pack(padx=5, pady=5)

        frame_util = tk.Frame(master=window)

        tk.Label(master=window, text="Enter Utility Costs").pack()

        lbl_power = tk.Label(master=frame_util, text="Power", width=15)
        entry_power = tk.Entry(master=frame_util)
        lbl_water = tk.Label(master=frame_util, text="Water", width=15)
        entry_water = tk.Entry(master=frame_util)
        lbl_internet = tk.Label(master=frame_util, text="Internet", width=15)
        entry_internet = tk.Entry(master=frame_util)
        lbl_fuel = tk.Label(master=frame_util, text="Fuel", width=15)
        entry_fuel = tk.Entry(master=frame_util)
        lbl_rent = tk.Label(master=frame_util, text="Rent", width=15)
        entry_rent = tk.Entry(master=frame_util)

        lbl_power.pack()
        entry_power.pack()
        lbl_water.pack()
        entry_water.pack()
        lbl_internet.pack()
        entry_internet.pack()
        lbl_fuel.pack()
        entry_fuel.pack()
        lbl_rent.pack()
        entry_rent.pack()

        frame_util.pack(padx=5, pady=5)

        frame_update = tk.Frame(master=window)

        update_btn = tk.Button(
            master=frame_update,
            text="Update DataFrame",
            command=lambda: self.update(Day=int(select_day.get()),
                                        Month=int(select_month.get()),
                                        Food=format_input(entry_food.get()),
                                        Item=format_input(entry_item.get()),
                                        Power=format_input(entry_power.get()),
                                        Water=format_input(entry_water.get()),
                                        Internet=format_input(entry_internet.get()),
                                        Fuel=format_input(entry_fuel.get()),
                                        Rent=format_input(entry_rent.get())
                                        )
        )

        update_btn.pack()

        frame_update.pack()

        frame_option = tk.Frame(master=window)

        tk.Label(master=window, text="Options").pack()

        save_btn = tk.Button(
            master=frame_option,
            text="Save to CSV",
            command=lambda: self.save()
        )

        total_btn = tk.Button(
            master=frame_option,
            text="Generate Totals",
            command=lambda: self.tally_up()
        )

        exit_btn = tk.Button(
            master=frame_option,
            text="Exit to Start",
            command=lambda: self.start(window)
        )

        exit_btn.grid(row=0, column=2, padx=5)
        total_btn.grid(row=0, column=1, padx=5)
        save_btn.grid(row=0, column=0, padx=5)

        frame_option.pack(padx=5, pady=5)

        window.mainloop()


# What we learned
# In future, the various pages should be classes so that we can benefit from class variables

if __name__ == "__main__":
    tax = Tax()
    tax.init()
