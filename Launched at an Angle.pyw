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
    V0i = V0i_entry.get()
    A0 = A0_entry.get()
    Hi = Hi_entry.get()
    Hf = Hf_entry.get()
    Tuser = Tuser_entry.get()

    # Entry Checks
    if V0i == "":
        V0i = 0
        V0i_test = True
    else:
        try:
            V0i = float(V0i)
            V0i_test = True
        except ValueError:
            V0i_test = False

    if A0 == "":
        A0 = 0
        A0_test = True
    else:
        try:
            A0 = float(A0)
            A0_test = True
        except ValueError:
            A0_test = False

    if Hi == "":
        Hi = 0
        Hi_test = True
    else:
        try:
            Hi = float(Hi)
            Hi_test = True
        except ValueError:
            Hi_test = False

    if Hf == "":
        Hf = 0
        Hf_test = True
    else:
        try:
            Hf = float(Hf)
            Hf_test = True
        except ValueError:
            Hf_test = False

    try:
        Tuser = float(Tuser)
        Tuser_test = True
    except ValueError:
        Tuser_test = False

    if V0i_test and A0_test and Hi_test and Hf_test:
        Velocity_test = True
    else:
        Velocity_test = False

    # Do Math
    if Velocity_test:
        # Initial Velocities
        Vyi = V0i * math.sin(math.radians(A0))
        Vxi = V0i * math.cos(math.radians(A0))
        Vyf = -1 * Vyi
        Vf = math.sqrt((Vyf ** 2) + (Vxi ** 2))

        # Flight Time
        Ttotal = (Vyf - Vyi) / g

        # Distance Traveled
        Dxtotal = Ttotal * Vxi

        # Time to Highest Point
        Thalf = Ttotal / 2

        # Max Height
        Dymax = (.5 * g * (Thalf ** 2)) + (Vyi * Thalf) + Hi

        if A0 > 90 or A0 < 0:
            result_label_main = Label(result_frame, justify=CENTER,
                                      text="Launch Angle MUST be between 0 and 90", fg="red")
        else:
            rr = int(rr)
            result_label_main = Label(result_frame, justify=CENTER,
                                      text=f'For a projectile launched at {round(V0i, rr)} m/s at {round(A0, rr)}°, '
                                      f'starting from {round(Hi, rr)} m and landing at {round(Hf, rr)} m:\n\n'
                                      f'Initial Vertical Velocity: {round(Vyi, rr)} m/s\n'
                                      f'Constant Horizontal Velocity: {round(Vxi, rr)} m/s\n'
                                      f'Final Vertical Velocity: {round(Vyf, rr)} m/s\n'
                                      f'True Final Velocity: {round(Vf, rr)} m/s\n\n'
                                      f'Total Flight Time: {round(Ttotal, rr)} seconds\n'
                                      f'Time to Highest Point: {round(Thalf, rr)} seconds\n'
                                      f'Max Height: {round(Dymax, rr)} meters\n'
                                      f'Distance Traveled: {round(Dxtotal, rr)} meters\n'
                                      f'_______________________________________________________________________________'
                                           f'__________________________________')



            steps = Dxtotal / 10
            if Dxtotal > Dymax:
                scale = 400/(Dxtotal)
            else:
                scale = 400/(Dymax)

            polygon_coords = scale*0, 400-0, \
                             scale*0, 400-0, \
                             scale*steps*1, 400-(scale*((.5*g*(((steps*1)/Vxi)**2))+(Vyi*((steps*1)/Vxi))+Hi)), \
                             scale*steps*2, 400-(scale*((.5*g*(((steps*2)/Vxi)**2))+(Vyi*((steps*2)/Vxi))+Hi)), \
                             scale*steps*3, 400-(scale*((.5*g*(((steps*3)/Vxi)**2))+(Vyi*((steps*3)/Vxi))+Hi)), \
                             scale*steps*4, 400-(scale*((.5*g*(((steps*4)/Vxi)**2))+(Vyi*((steps*4)/Vxi))+Hi)), \
                             scale*steps*5, 400-(scale*((.5*g*(((steps*5)/Vxi)**2))+(Vyi*((steps*5)/Vxi))+Hi)), \
                             scale*steps*6, 400-(scale*((.5*g*(((steps*6)/Vxi)**2))+(Vyi*((steps*6)/Vxi))+Hi)), \
                             scale*steps*7, 400-(scale*((.5*g*(((steps*7)/Vxi)**2))+(Vyi*((steps*7)/Vxi))+Hi)), \
                             scale*steps*8, 400-(scale*((.5*g*(((steps*8)/Vxi)**2))+(Vyi*((steps*8)/Vxi))+Hi)), \
                             scale*steps*9, 400-(scale*((.5*g*(((steps*9)/Vxi)**2))+(Vyi*((steps*9)/Vxi))+Hi)), \
                             scale*steps*10, 400-0, \
                             scale*steps*10, 400-0
            graph_canvas.coords(position_arc, polygon_coords)

            if Tuser_test:
                # Velocity at any Time
                Vyu = (g * Tuser) + Vyi
                Vxu = Vxi
                Vu = math.sqrt((Vyu ** 2) + (Vxu ** 2))

                # Distance to any Time
                Dxu = Tuser * Vxi

                # Height at any Time
                Dyu = (.5 * g * (Tuser ** 2)) + (Vyi * Tuser) + Hi

                if Tuser_entry.get() == "":
                    result_label_Tuser = Label(result_frame, justify=CENTER,
                                               text="")
                elif not Tuser_test or Tuser < 0 or Tuser > Ttotal:
                    result_label_Tuser = Label(result_frame, justify=CENTER,
                                               text="Custom Time MUST be between 0 and Total Flight Time", fg="red")
                else:
                    result_label_Tuser = Label(result_frame, justify=CENTER,
                                               text=f'Vertical Velocity at {round(Tuser, rr)} s: {round(Vyu, rr)} m/s\n'
                                                    f'Horizontal Velocity at {round(Tuser, rr)} s: {round(Vxu, rr)} m/s\n'
                                                    f'True Velocity at {round(Tuser, rr)} s: {round(Vu, rr)} m/s\n\n'
                                                    f'Distance Traveled at {round(Tuser, rr)} s: {round(Dxu, rr)} m\n'
                                                    f'Height at {round(Tuser, rr)} s: {round(Dyu, rr)} m')

                    custom_coords = scale*Dxu, 400-0, \
                                    scale*Dxu, 400-(scale*((.5*g*(((Dxu)/Vxi)**2))+(Vyi*((Dxu)/Vxi))+Hi))
                    graph_canvas.coords(custom_line, custom_coords)

            elif Tuser_entry.get() == "":
                result_label_Tuser = Label(result_frame, justify=CENTER,
                                           text="")
                graph_canvas.coords(custom_line, 0, 0, 0, 0)
            else:
                result_label_Tuser = Label(result_frame, justify=CENTER,
                                           text="Custom Time MUST be a number", fg="red")
                graph_canvas.coords(custom_line, 0, 0, 0, 0)
            result_label_Tuser.grid(row=1, column=0, pady=5)
    else:
        result_label_main = Label(result_frame, justify=CENTER,
                                  text="Inputs MUST be numbers", fg="red")

    result_label_main.grid(row=0, column=0, padx=10)
    print(text_frame.winfo_width())


root = Tk()
root.title("Physics: Launched at an Angle")
root.geometry("1000x404")
root.resizable(0, 0)


# Text Frame
text_frame = Frame(root)
text_frame.pack(side=LEFT)

# Title frame
title_frame = Frame(text_frame)
title_frame.pack(side=TOP, fill=X)

title_txt = Label(title_frame, text="Physics: Launched at an Angle", font=('Helvetica', 10, 'bold'))
title_txt.pack(pady=10, padx=10)

# Entry Frame
entry_frame = Frame(text_frame)
entry_frame.pack()

V0i_label = Label(entry_frame, text="Initial Velocity")
A0_label = Label(entry_frame, text="Launch Angle")
Hi_label = Label(entry_frame, text="Initial Height")
Hf_label = Label(entry_frame, text="Starting Height")
Tuser_label = Label(entry_frame, text="Custom Time")
round_label = Label(entry_frame, text="Round Results")

V0i_var = StringVar()
A0_var = StringVar()
Hi_var = StringVar()
Hf_var = StringVar()
Tuser_var = StringVar()
round_var = StringVar()

V0i_entry = Entry(entry_frame, textvariable=V0i_var)
A0_entry = Entry(entry_frame, textvariable=A0_var)
Hi_entry = Entry(entry_frame, textvariable=Hi_var)
Hf_entry = Entry(entry_frame, textvariable=Hf_var)
Tuser_entry = Entry(entry_frame, textvariable=Tuser_var)
round_entry = Scale(entry_frame, from_=0, to=10, orient=HORIZONTAL, showvalue=0, sliderlength=20, length=125, variable=round_var)

V0i_label.grid(row=0, column=0, pady=1)
A0_label.grid(row=0, column=2, pady=1)
Hi_label.grid(row=1, column=0, pady=1)
Hf_label.grid(row=1, column=2, pady=1)
Tuser_label.grid(row=2, column=0, pady=1)
round_label.grid(row=2, column=2, pady=1)

V0i_entry.grid(row=0, column=1, pady=1)
V0i_entry.focus()
A0_entry.grid(row=0, column=3, pady=1)
Hi_entry.grid(row=1, column=1, pady=1)
Hf_entry.grid(row=1, column=3, pady=1)
Tuser_entry.grid(row=2, column=1, pady=1)
round_entry.grid(row=2, column=3, pady=1)

# Entry Default Values
V0i_entry.insert(0, "10")
A0_entry.insert(0, "45")
Hi_entry.insert(0, "0")
Hf_entry.insert(0, "0")
Tuser_entry.insert(0, "")
round_entry.set(2)

# Result Frame
result_frame = Frame(text_frame)
result_frame.pack()

V0i_var.trace_add("write", calculate)
A0_var.trace_add("write", calculate)
Hi_var.trace_add("write", calculate)
Hf_var.trace_add("write", calculate)
Tuser_var.trace_add("write", calculate)
round_var.trace_add("write", calculate)

# Graph Frame
graph_frame = Frame(root)
graph_frame.pack(side=RIGHT)

# Graph
c_h = 400
c_w = 400
graph_canvas = Canvas(graph_frame, bg="white", height=c_h, width=c_w)
graph_canvas.pack()

position_arc = graph_canvas.create_polygon(0, 0, fill='', outline='black', smooth=1)
custom_line = graph_canvas.create_line(0, 0, 0, 0)
ground_line = graph_canvas.create_line(0, 400, 400, 400)

calculate()
mainloop()
