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
    Vyi = Vyi_entry.get()
    TimeT = TimeT_entry.get()
    Xuser = Xuser_entry.get()

    # Entry Checks
    if Vyi == "":
        Vyi = 0
        Vyi_test = True
    else:
        try:
            Vyi = float(Vyi)
            Vyi_test = True
        except ValueError:
            Vyi_test = False

    if TimeT == "":
        TimeT = 0
        Timet_test = True
    else:
        try:
            TimeT = float(TimeT)
            Timet_test = True
        except ValueError:
            Timet_test = False

    try:
        Xuser = float(Xuser)
        Xuser_test = True
    except ValueError:
        Xuser_test = False

    if Vyi_test and Timet_test and Xuser_test:
        Velocity_test = True
    else:
        Velocity_test = False

    # Do Math
    if Velocity_test:
        # Calculations
        distance_to_ground = (.5 * g * (TimeT ** 2)) + (Vyi * TimeT)
        Vyf = (g * TimeT) + Vyi
        Dx = Xuser * TimeT

        if TimeT < 0:
            result_label_main = Label(result_frame, justify=CENTER,
                                      text="Drop Time MUST be greater than 0\n\n\n\n\n\n", fg="red")
        else:
            rr = int(rr)
            result_label_main = Label(result_frame, justify=CENTER,
                                      text=f'For an object that dropped off a cliff at {round(Vyi, rr)}'
                                           f'm/s vertically and hit the ground in {round(TimeT, rr)}s:\n'
                                           f'Distance to Ground: {round(distance_to_ground, rr)}m\n'
                                           f'Final Vertical Velocity: {round(Vyf, rr)}m/s\n\n'
                                           f'If the object also had a horizontal velocity of {round(Xuser, rr)}m/s:\n'
                                           f'Horizontal Displacement: {round(Dx, rr)}m')
    else:
        result_label_main = Label(result_frame, justify=CENTER,
                                  text="Inputs MUST be numbers\n\n\n\n\n\n", fg="red")

    result_label_main.grid(row=0, column=0, padx=10)
    # print(root.winfo_width())
    # print(root.winfo_height())


root = Tk()
root.title("Physics: Distance to Ground from Drop TIme")
root.geometry("476x186")
root.resizable(0, 0)


# Text Frame
text_frame = Frame(root)
text_frame.pack(side=LEFT)

# Title frame
title_frame = Frame(text_frame)
title_frame.pack(side=TOP, fill=X)

title_txt = Label(title_frame, text="Physics: Distance to Ground from Drop Time", font=('Helvetica', 10, 'bold'))
title_txt.pack(pady=10, padx=10)

# Entry Frame
entry_frame = Frame(text_frame)
entry_frame.pack()

Vyi_label = Label(entry_frame, text="Initial Vertical Velocity")
TimeT_label = Label(entry_frame, text="Drop Time")
Xuser_label = Label(entry_frame, text="Horizontal Velocity")
round_label = Label(entry_frame, text="Round Results")

Vyi_var = StringVar()
TimeT_var = StringVar()
Xuser_var = StringVar()
round_var = StringVar()

Vyi_entry = Entry(entry_frame, textvariable=Vyi_var)
TimeT_entry = Entry(entry_frame, textvariable=TimeT_var)
Xuser_entry = Entry(entry_frame, textvariable=Xuser_var)
round_entry = Scale(entry_frame, from_=0, to=10, orient=HORIZONTAL, showvalue=0, sliderlength=20, length=125, variable=round_var)

Vyi_label.grid(row=0, column=0, pady=1)
TimeT_label.grid(row=0, column=2, pady=1)
Xuser_label.grid(row=1, column=0, pady=1)
round_label.grid(row=1, column=2, pady=1)

Vyi_entry.grid(row=0, column=1, pady=1)
Vyi_entry.focus()
TimeT_entry.grid(row=0, column=3, pady=1)
Xuser_entry.grid(row=1, column=1, pady=1)
round_entry.grid(row=1, column=3, pady=1)

# Entry Default Values
Vyi_entry.insert(0, "0")
TimeT_entry.insert(0, "5")
Xuser_entry.insert(0, "0")
round_entry.set(2)

# Result Frame
result_frame = Frame(text_frame)
result_frame.pack()

Vyi_var.trace_add("write", calculate)
TimeT_var.trace_add("write", calculate)
Xuser_var.trace_add("write", calculate)
round_var.trace_add("write", calculate)

calculate()
mainloop()
