# Written by Matthew DiMaggio
# Created 9/29/2021

from tkinter import *
import math


def calculate(*args):
    for child in result_frame.winfo_children():
        child.destroy()

    rr = round_entry.get()

    # Constants
    g = -9.8

    # Inputs
    Vi = Vi_entry.get()
    Vf = Vf_entry.get()
    Dx = Dx_entry.get()

    # Entry Checks
    if Vi == "":
        Vi = 0
        Vi_test = True
    else:
        try:
            Vi = float(Vi)
            Vi_test = True
        except ValueError:
            Vi_test = False

    if Vf == "":
        Vf = 0
        Vf_test = True
    else:
        try:
            Vf = float(Vf)
            Vf_test = True
        except ValueError:
            Vf_test = False

    try:
        Dx = float(Dx)
        Dx_test = True
    except ValueError:
        Dx_test = False

    if Vi_test and Vf_test and Dx_test:
        Velocity_test = True
    else:
        Velocity_test = False

    # Do Math
    if Velocity_test:
        # Calculations
        acc = ((Vf ** 2) - (Vi ** 2)) / (2 * Dx)

        rr = int(rr)
        result_label_main = Label(result_frame, justify=CENTER,
                                  text=f'If an object changed velocities from {round(Vi, rr)}m/s to {round(Vf, rr)}m/s'
                                       f' in {round(Dx, rr)}m:\n\n'
                                       f'Acceleration: {acc}')
    else:
        result_label_main = Label(result_frame, justify=CENTER,
                                  text="Inputs MUST be numbers\n\n", fg="red")

    result_label_main.grid(row=0, column=0, padx=10)
    # print(root.winfo_width())
    # print(root.winfo_height())


root = Tk()
root.title("Physics: Acceleration from Velocity and Displacement")
root.geometry("476x186")
root.resizable(0, 0)


# Text Frame
text_frame = Frame(root)
text_frame.pack(side=LEFT)

# Title frame
title_frame = Frame(text_frame)
title_frame.pack(side=TOP, fill=X)

title_txt = Label(title_frame, text="Physics: Acceleration from Velocity and Displacement", font=('Helvetica', 10, 'bold'))
title_txt.pack(pady=10, padx=10)

# Entry Frame
entry_frame = Frame(text_frame)
entry_frame.pack()

Vi_label = Label(entry_frame, text="Initial Velocity")
Vf_label = Label(entry_frame, text="Final Velocity")
Dx_label = Label(entry_frame, text="Displacement")
round_label = Label(entry_frame, text="Round Results")

Vi_var = StringVar()
Vf_var = StringVar()
Dx_var = StringVar()
round_var = StringVar()

Vi_entry = Entry(entry_frame, textvariable=Vi_var)
Vf_entry = Entry(entry_frame, textvariable=Vf_var)
Dx_entry = Entry(entry_frame, textvariable=Dx_var)
round_entry = Scale(entry_frame, from_=0, to=10, orient=HORIZONTAL, showvalue=0, sliderlength=20, length=125, variable=round_var)

Vi_label.grid(row=0, column=0, pady=1)
Vf_label.grid(row=0, column=2, pady=1)
Dx_label.grid(row=1, column=0, pady=1)
round_label.grid(row=1, column=2, pady=1)

Vi_entry.grid(row=0, column=1, pady=1)
Vi_entry.focus()
Vf_entry.grid(row=0, column=3, pady=1)
Dx_entry.grid(row=1, column=1, pady=1)
round_entry.grid(row=1, column=3, pady=1)

# Entry Default Values
Vi_entry.insert(0, "0")
Vf_entry.insert(0, "5")
Dx_entry.insert(0, "1")
round_entry.set(2)

# Result Frame
result_frame = Frame(text_frame)
result_frame.pack()

Vi_var.trace_add("write", calculate)
Vf_var.trace_add("write", calculate)
Dx_var.trace_add("write", calculate)
round_var.trace_add("write", calculate)

calculate()
mainloop()
