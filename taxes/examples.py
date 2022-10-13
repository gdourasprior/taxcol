# This is a sample Python script.
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

window = tk.Tk()

# ------ Example 1

# frame = tk.Frame(master=window, width=150, height=150, borderwidth=5)
# frame_a = tk.Frame(master=frame, relief=tk.GROOVE, borderwidth=10)
# frame_b = tk.Frame(master=frame, relief=tk.SUNKEN, borderwidth=5)
#
# frame.pack()
#
# label1 = tk.Label(master=frame, text="I'm at (50, 100)", bg="red")
# label1.place(x=50, y=100)
#
# label2 = tk.Label(master=frame, text="I'm at (100, 50)", bg="yellow")
# label2.place(x=100, y=50)
#
# frame_a.pack(
#     side=tk.LEFT,
#     fill=tk.BOTH,
#     expand=True
# )
# frame_b.pack(
#     side=tk.LEFT,
#     fill=tk.BOTH,
#     expand=True
# )
#
# greetings = tk.Label(
#     text="Hello, Tkinter",
#     foreground="white",
#     bg="#34A2FE",
#     width=10,  # Determined by 'text units', this width is ten '0' and height is 10 lines of '0'
#     height=10,
#     master=frame_a
# )
# greetings.pack()
#
# entry = tk.Entry(
#     fg="yellow",
#     background="blue",
#     width=50,
#     master=frame_b
# )
# entry.pack()
#
# button = tk.Button(
#     text="Click me!",
#     width=25,
#     height=5,
#     bg="blue",
#     foreground="yellow",
#     master=frame_b
# )
# button.pack()

# ------ Example 2

# for i in range(3):
#     window.columnconfigure(i, weight=1, minsize=75)
#     window.rowconfigure(i, weight=1, minsize=50)
#     for j in range(3):
#         frame = tk.Frame(
#             master=window,
#             relief=tk.RAISED,
#             borderwidth=1
#         )
#         frame.grid(row=i, column=j, padx=5, pady=5)
#         label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
#         label.pack(padx=5, pady=5)  # Same result as padding in 'grid'


# ------ Example 3

# window.columnconfigure(0, minsize=250)
# window.rowconfigure([0, 1], minsize=100)
#
# label1 = tk.Label(text="A")
# label1.grid(row=0, column=0, sticky="ne")
#
# label2 = tk.Label(text="B")
# label2.grid(row=1, column=0, sticky="sw")


# ------ Example 4  (grid is most commonly used and most flexible of the 'geometry managers'

# window.rowconfigure(0, minsize=50)
# window.columnconfigure([0, 1, 2, 3], minsize=50)
#
# label1 = tk.Label(text="1", bg="black", fg="white")
# label2 = tk.Label(text="2", bg="black", fg="white")
# label3 = tk.Label(text="3", bg="black", fg="white")
# label4 = tk.Label(text="4", bg="black", fg="white")
#
# label1.grid(row=0, column=0)
# label2.grid(row=0, column=1, sticky="ew")  # Functionally identical to .pack(fill=tk.X)
# label3.grid(row=0, column=2, sticky="ns")  # Functionally identical to .pack(fill=tk.Y)
# label4.grid(row=0, column=3, sticky="nsew")  # Functionally identical to .pack(fill=tk.BOTH)

# ------ Example 5 (Interactive UI via Events and Handlers)

# def handle_keypress(event):
#     print(event.char)
#
#
# def handle_click(event):
#     print("Button clicked")
#
#
# button = tk.Button(text="Click me!")
#
# window.bind("<Key>", handle_keypress)
# button.bind("<Button-1>", handle_click)
#
# button.pack()


# ------ Example 6 (Interactive UI cont. Using commands)

# def increase_lbl_val():
#     value = int(lbl_value["text"])
#     lbl_value["text"] = f"{value + 1}"
#
#
# def decrease_lbl_val():
#     value = int(lbl_value["text"])
#     lbl_value["text"] = f"{value - 1}"
#
#
# window.rowconfigure(0, minsize=50, weight=1)
# window.columnconfigure([0, 1, 2], minsize=50, weight=1)
#
# btn_decrease = tk.Button(master=window, text="-", command=decrease_lbl_val)
# btn_decrease.grid(row=0, column=0, sticky="nesw")
#
# lbl_value = tk.Label(master=window, text="0")
# lbl_value.grid(row=0, column=1)
#
# btn_increase = tk.Button(master=window, text="+", command=increase_lbl_val)
# btn_increase.grid(row=0, column=2, sticky="nesw")


# ------ Example 7 (Example App: Temperature Conversion)

# window.title("Temperature Converter")
# window.resizable(width=False, height=False)
#
#
# def convert_f_to_c():
#     value = ent_temp.get()
#
#     result = (float(value) - 32) / (9/5)
#
#     lbl_result["text"] = f"{round(result, 3)} \N{DEGREE CELSIUS}"
#
#
# window.rowconfigure(0, minsize=50, weight=1)
# window.columnconfigure([0, 1, 2], minsize=50, weight=1)
#
# frm_entry = tk.Frame(master=window)
#
# ent_temp = tk.Entry(master=frm_entry, width=10, relief=tk.FLAT)
# ent_temp.grid(row=0, column=0, sticky="e")
#
# lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}", relief=tk.FLAT)
# lbl_temp.grid(row=0, column=1, sticky="w")
#
# frm_entry.grid(row=0, column=0, padx=10)
#
# btn_convert = tk.Button(
#     master=window,
#     text="Convert \N{RIGHTWARDS BLACK ARROW}",
#     relief=tk.SUNKEN,
#     bg="grey", fg="green",
#     command=convert_f_to_c
# )
# btn_convert.grid(row=0, column=1, padx=10)
#
# lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")
# lbl_result.grid(row=0, column=2, padx=10)


# ------- Example 8 (TEXT EDITOR, Save, Load, Edit and Open a given file)

# def open_file():
#     filepath = askopenfilename(
#         filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
#     )
#     if not filepath:
#         return
#     txt_edit.delete("1.0", tk.END)
#     with open(filepath, mode="r", encoding="utf-8") as input_file:
#         text = input_file.read()
#         txt_edit.insert(tk.END, text)
#     window.title(f"Simple Text Editor - {filepath}")
#
#
# def save_file():
#     filepath = asksaveasfilename(
#         defaultextension=".txt",
#         filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
#     )
#     if not filepath:
#         return
#     with open(filepath, mode="w", encoding="utf-8") as output_file:
#         text = txt_edit.get("1.0", tk.END)
#         output_file.write(text)
#     window.title(f"Simple Text Editor - {filepath}")
#
#
# window.title("Simple Text Editor")
#
# window.rowconfigure(0, minsize=800, weight=1)
# window.columnconfigure(1, minsize=800, weight=1)
#
# txt_edit = tk.Text(window)
#
# frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
#
# btn_open = tk.Button(frm_buttons, text="Open", command=open_file)
# btn_save = tk.Button(frm_buttons, text="Save As...", command=save_file)
#
# btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
# btn_save.grid(row=1, column=0, sticky="ew", padx=5)
#
# frm_buttons.grid(row=0, column=0, sticky="ns")
# txt_edit.grid(row=0, column=1, sticky="nesw")
#
#
# window.mainloop()  # Required to have window appear

# ---- Test, Window swapping

# def init():
#     window = tk.Tk()
#     window.rowconfigure(0, minsize=800, weight=1)
#     window.columnconfigure(1, minsize=800, weight=1)
#
#     button = tk.Button(
#         master=window,
#         text="Click Here!",
#         command=lambda: win_02(window)
#     )
#     button.pack()
#
#     window.mainloop()  # Required to have window appear
#
#
# def win_02(current):
#     current.destroy()
#     window = tk.Tk()
#     window.rowconfigure(0, minsize=800, weight=1)
#     window.columnconfigure(1, minsize=800, weight=1)
#
#     button = tk.Button(
#         master=window,
#         text="Click Here!",
#         command=lambda: win_01(window)
#     )
#     button.pack()
#
#     window.mainloop()
#
#
# def win_01(current):
#     current.destroy()
#     init()
#

import pandas as pd
import numpy as np



_COLUMNS = ["Data", "Food", "Items", "Power", "Water", "Internet", "Fuel"]

_DICT = dict.fromkeys(_COLUMNS)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(_DICT)
    temp = pd.DataFrame.from_dict(kwargs)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
