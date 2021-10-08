from tkinter import *
from functools import partial


def calculate(*args):

    rr = round_input.get()

    # Constants
    G = 6.67e-11

    m1 = float(mass1_var.get())
    m1SN = int(mass1SN_var.get())
    m2 = float(mass2_var.get())
    m2SN = int(mass2SN_var.get())
    r = float(radius_var.get())
    rSN = int(radiusSN_var.get())

    m1c = m1*(10**m1SN)
    m2c = m2*(10**m2SN)
    rc = r*(10**rSN)

    Fg = (G * m1c * m2c) / (rc ** 2)
    gm1 = Fg / m1c
    gm2 = Fg / m2c

    result_label.configure(text=f'Gravitational Force = {round(Fg, rr)}N\n'
                                f'Acceleration of Mass 1 to Mass 2 = {round(gm1, rr)}m/s²\n'
                                f'Acceleration of Mass 2 to Mass 1 = {round(gm2, rr)}m/s²')



root = Tk()
root.wait_visibility()
root.title("Universal Gravitation")

# Library Frame


class LibraryMenu(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)

        sunmass = ["1.989", "30"]
        mercurymass = ["3.30", "23"]
        venusmass = ["4.87", "24"]
        earthmass = ["5.97", "24"]
        marsmass = ["6.42", "23"]
        jupitermass = ["1.898", "27"]
        saturnmass = ["5.68", "26"]
        uranusmass = ["8.68", "25"]
        neptunemass = ["1.02", "26"]
        plutomass = ["1.46", "22"]

        sunrad = ["6.96347055", "8"]
        mercuryrad = ["2.44", "6", "5.79", "10"]
        venusrad = ["6.052", "6", "1.082", "11"]
        earthrad = ["1.276", "7", "1.496", "11"]
        marsrad = ["3.396", "6", "2.279", "11"]
        jupiterrad = ["1.43", "8", "7.786", "11"]
        saturnrad = ["1.205", "8", "1.434", "12"]
        uranusrad = ["5.112", "7", "2.873", "12"]
        neptunerad = ["4.953", "7", "4.495", "12"]
        plutorad = ["1.185", "6", "5.906", "12"]

        # Planetary Info from https://nssdc.gsfc.nasa.gov/planetary/factsheet/

        def sunreplace(i):
            if i == 0:
                mass1_input.delete(0, len(mass1_var.get()))
                mass1SN_input.delete(0, len(mass1SN_var.get()))
                mass1_input.insert(0, sunmass[0])
                mass1SN_input.insert(0, sunmass[1])
            elif i == 1:
                mass2_input.delete(0, len(mass2_var.get()))
                mass2SN_input.delete(0, len(mass2SN_var.get()))
                mass2_input.insert(0, sunmass[0])
                mass2SN_input.insert(0, sunmass[1])
            elif i == 2:
                radius_input.delete(0, len(radius_var.get()))
                radiusSN_input.delete(0, len(radiusSN_var.get()))
                radius_input.insert(0, sunrad[0])
                radiusSN_input.insert(0, sunrad[1])
            else:
                print("ERROR")

        def mercuryreplace(i):
            if i == 0:
                mass1_input.delete(0, len(mass1_var.get()))
                mass1SN_input.delete(0, len(mass1SN_var.get()))
                mass1_input.insert(0, mercurymass[0])
                mass1SN_input.insert(0, mercurymass[1])
            elif i == 1:
                mass2_input.delete(0, len(mass2_var.get()))
                mass2SN_input.delete(0, len(mass2SN_var.get()))
                mass2_input.insert(0, mercurymass[0])
                mass2SN_input.insert(0, mercurymass[1])
            elif i == 2:
                radius_input.delete(0, len(radius_var.get()))
                radiusSN_input.delete(0, len(radiusSN_var.get()))
                radius_input.insert(0, mercuryrad[0])
                radiusSN_input.insert(0, mercuryrad[1])
            elif i == 3:
                radius_input.delete(0, len(radius_var.get()))
                radiusSN_input.delete(0, len(radiusSN_var.get()))
                radius_input.insert(0, mercuryrad[2])
                radiusSN_input.insert(0, mercuryrad[3])
            else:
                print("ERROR")

        def venusreplace(i):
            if i == 0:
                mass1_input.delete(0, len(mass1_var.get()))
                mass1SN_input.delete(0, len(mass1SN_var.get()))
                mass1_input.insert(0, venusmass[0])
                mass1SN_input.insert(0, venusmass[1])
            elif i == 1:
                mass2_input.delete(0, len(mass2_var.get()))
                mass2SN_input.delete(0, len(mass2SN_var.get()))
                mass2_input.insert(0, venusmass[0])
                mass2SN_input.insert(0, venusmass[1])
            elif i == 2:
                radius_input.delete(0, len(radius_var.get()))
                radiusSN_input.delete(0, len(radiusSN_var.get()))
                radius_input.insert(0, venusrad[0])
                radiusSN_input.insert(0, venusrad[1])
            elif i == 3:
                radius_input.delete(0, len(radius_var.get()))
                radiusSN_input.delete(0, len(radiusSN_var.get()))
                radius_input.insert(0, venusrad[2])
                radiusSN_input.insert(0, venusrad[3])
            else:
                print("ERROR")

        def earthreplace(i):
            if i == 0:
                mass1_input.delete(0, len(mass1_var.get()))
                mass1SN_input.delete(0, len(mass1SN_var.get()))
                mass1_input.insert(0, earthmass[0])
                mass1SN_input.insert(0, earthmass[1])
            elif i == 1:
                mass2_input.delete(0, len(mass2_var.get()))
                mass2SN_input.delete(0, len(mass2SN_var.get()))
                mass2_input.insert(0, earthmass[0])
                mass2SN_input.insert(0, earthmass[1])
            elif i == 2:
                radius_input.delete(0, len(radius_var.get()))
                radiusSN_input.delete(0, len(radiusSN_var.get()))
                radius_input.insert(0, earthrad[0])
                radiusSN_input.insert(0, earthrad[1])
            elif i == 3:
                radius_input.delete(0, len(radius_var.get()))
                radiusSN_input.delete(0, len(radiusSN_var.get()))
                radius_input.insert(0, earthrad[2])
                radiusSN_input.insert(0, earthrad[3])
            else:
                print("ERROR")

        def marsreplace(i):
            if i == 0:
                mass1_input.delete(0, len(mass1_var.get()))
                mass1SN_input.delete(0, len(mass1SN_var.get()))
                mass1_input.insert(0, marsmass[0])
                mass1SN_input.insert(0, marsmass[1])
            elif i == 1:
                mass2_input.delete(0, len(mass2_var.get()))
                mass2SN_input.delete(0, len(mass2SN_var.get()))
                mass2_input.insert(0, marsmass[0])
                mass2SN_input.insert(0, marsmass[1])
            elif i == 2:
                radius_input.delete(0, len(radius_var.get()))
                radiusSN_input.delete(0, len(radiusSN_var.get()))
                radius_input.insert(0, marsrad[0])
                radiusSN_input.insert(0, marsrad[1])
            elif i == 3:
                radius_input.delete(0, len(radius_var.get()))
                radiusSN_input.delete(0, len(radiusSN_var.get()))
                radius_input.insert(0, marsrad[2])
                radiusSN_input.insert(0, marsrad[3])
            else:
                print("ERROR")

        def jupiterreplace(i):
            if i == 0:
                mass1_input.delete(0, len(mass1_var.get()))
                mass1SN_input.delete(0, len(mass1SN_var.get()))
                mass1_input.insert(0, jupitermass[0])
                mass1SN_input.insert(0, jupitermass[1])
            elif i == 1:
                mass2_input.delete(0, len(mass2_var.get()))
                mass2SN_input.delete(0, len(mass2SN_var.get()))
                mass2_input.insert(0, jupitermass[0])
                mass2SN_input.insert(0, jupitermass[1])
            elif i == 2:
                radius_input.delete(0, len(radius_var.get()))
                radiusSN_input.delete(0, len(radiusSN_var.get()))
                radius_input.insert(0, jupiterrad[0])
                radiusSN_input.insert(0, jupiterrad[1])
            elif i == 3:
                radius_input.delete(0, len(radius_var.get()))
                radiusSN_input.delete(0, len(radiusSN_var.get()))
                radius_input.insert(0, jupiterrad[2])
                radiusSN_input.insert(0, jupiterrad[3])
            else:
                print("ERROR")

        def saturnreplace(i):
            if i == 0:
                mass1_input.delete(0, len(mass1_var.get()))
                mass1SN_input.delete(0, len(mass1SN_var.get()))
                mass1_input.insert(0, saturnmass[0])
                mass1SN_input.insert(0, saturnmass[1])
            elif i == 1:
                mass2_input.delete(0, len(mass2_var.get()))
                mass2SN_input.delete(0, len(mass2SN_var.get()))
                mass2_input.insert(0, saturnmass[0])
                mass2SN_input.insert(0, saturnmass[1])
            elif i == 2:
                radius_input.delete(0, len(radius_var.get()))
                radiusSN_input.delete(0, len(radiusSN_var.get()))
                radius_input.insert(0, saturnrad[0])
                radiusSN_input.insert(0, saturnrad[1])
            elif i == 3:
                radius_input.delete(0, len(radius_var.get()))
                radiusSN_input.delete(0, len(radiusSN_var.get()))
                radius_input.insert(0, saturnrad[2])
                radiusSN_input.insert(0, saturnrad[3])
            else:
                print("ERROR")

        def uranusreplace(i):
            if i == 0:
                mass1_input.delete(0, len(mass1_var.get()))
                mass1SN_input.delete(0, len(mass1SN_var.get()))
                mass1_input.insert(0, uranusmass[0])
                mass1SN_input.insert(0, uranusmass[1])
            elif i == 1:
                mass2_input.delete(0, len(mass2_var.get()))
                mass2SN_input.delete(0, len(mass2SN_var.get()))
                mass2_input.insert(0, uranusmass[0])
                mass2SN_input.insert(0, uranusmass[1])
            elif i == 2:
                radius_input.delete(0, len(radius_var.get()))
                radiusSN_input.delete(0, len(radiusSN_var.get()))
                radius_input.insert(0, uranusrad[0])
                radiusSN_input.insert(0, uranusrad[1])
            elif i == 3:
                radius_input.delete(0, len(radius_var.get()))
                radiusSN_input.delete(0, len(radiusSN_var.get()))
                radius_input.insert(0, uranusrad[2])
                radiusSN_input.insert(0, uranusrad[3])
            else:
                print("ERROR")

        def neptunereplace(i):
            if i == 0:
                mass1_input.delete(0, len(mass1_var.get()))
                mass1SN_input.delete(0, len(mass1SN_var.get()))
                mass1_input.insert(0, neptunemass[0])
                mass1SN_input.insert(0, neptunemass[1])
            elif i == 1:
                mass2_input.delete(0, len(mass2_var.get()))
                mass2SN_input.delete(0, len(mass2SN_var.get()))
                mass2_input.insert(0, neptunemass[0])
                mass2SN_input.insert(0, neptunemass[1])
            elif i == 2:
                radius_input.delete(0, len(radius_var.get()))
                radiusSN_input.delete(0, len(radiusSN_var.get()))
                radius_input.insert(0, neptunerad[0])
                radiusSN_input.insert(0, neptunerad[1])
            elif i == 3:
                radius_input.delete(0, len(radius_var.get()))
                radiusSN_input.delete(0, len(radiusSN_var.get()))
                radius_input.insert(0, neptunerad[2])
                radiusSN_input.insert(0, neptunerad[3])
            else:
                print("ERROR")

        def plutoreplace(i):
            if i == 0:
                mass1_input.delete(0, len(mass1_var.get()))
                mass1SN_input.delete(0, len(mass1SN_var.get()))
                mass1_input.insert(0, plutomass[0])
                mass1SN_input.insert(0, plutomass[1])
            elif i == 1:
                mass2_input.delete(0, len(mass2_var.get()))
                mass2SN_input.delete(0, len(mass2SN_var.get()))
                mass2_input.insert(0, plutomass[0])
                mass2SN_input.insert(0, plutomass[1])
            elif i == 2:
                radius_input.delete(0, len(radius_var.get()))
                radiusSN_input.delete(0, len(radiusSN_var.get()))
                radius_input.insert(0, plutorad[0])
                radiusSN_input.insert(0, plutorad[1])
            elif i == 3:
                radius_input.delete(0, len(radius_var.get()))
                radiusSN_input.delete(0, len(radiusSN_var.get()))
                radius_input.insert(0, plutorad[2])
                radiusSN_input.insert(0, plutorad[3])
            else:
                print("ERROR")

        menubar = Menu(self, tearoff=0)
        lib_menu = Menu(self, tearoff=0)

        sunstuff_menu = Menu(self, tearoff=0)
        sunmass_menu = Menu(self, tearoff=0)
        mercurystuff_menu = Menu(self, tearoff=0)
        mercurymass_menu = Menu(self, tearoff=0)
        venusstuff_menu = Menu(self, tearoff=0)
        venusmass_menu = Menu(self, tearoff=0)
        earthstuff_menu = Menu(self, tearoff=0)
        earthmass_menu = Menu(self, tearoff=0)
        marsstuff_menu = Menu(self, tearoff=0)
        marsmass_menu = Menu(self, tearoff=0)
        jupiterstuff_menu = Menu(self, tearoff=0)
        jupitermass_menu = Menu(self, tearoff=0)
        saturnstuff_menu = Menu(self, tearoff=0)
        saturnmass_menu = Menu(self, tearoff=0)
        uranusstuff_menu = Menu(self, tearoff=0)
        uranusmass_menu = Menu(self, tearoff=0)
        neptunestuff_menu = Menu(self, tearoff=0)
        neptunemass_menu = Menu(self, tearoff=0)
        plutostuff_menu = Menu(self, tearoff=0)
        plutomass_menu = Menu(self, tearoff=0)

        menubar.add_cascade(label="Library", menu=lib_menu)
        lib_menu.add_cascade(label="Sun", menu=sunstuff_menu)
        lib_menu.add_cascade(label="Mercury", menu=mercurystuff_menu)
        lib_menu.add_cascade(label="Venus", menu=venusstuff_menu)
        lib_menu.add_cascade(label="Earth", menu=earthstuff_menu)
        lib_menu.add_cascade(label="Mars", menu=marsstuff_menu)
        lib_menu.add_cascade(label="Jupiter", menu=jupiterstuff_menu)
        lib_menu.add_cascade(label="Saturn", menu=saturnstuff_menu)
        lib_menu.add_cascade(label="Uranus", menu=uranusstuff_menu)
        lib_menu.add_cascade(label="Neptune", menu=neptunestuff_menu)
        lib_menu.add_cascade(label="Pluto", menu=plutostuff_menu)

        sunstuff_menu.add_cascade(label="Mass", menu=sunmass_menu)
        sunmass_menu.add_command(label="Insert for Mass 1", command=partial(sunreplace, 0))
        sunmass_menu.add_command(label="Insert for Mass 2",command=partial(sunreplace, 1))
        sunstuff_menu.add_command(label="Radius", command=partial(sunreplace, 2))

        mercurystuff_menu.add_cascade(label="Mass", menu=mercurymass_menu)
        mercurymass_menu.add_command(label="Insert for Mass 1", command=partial(mercuryreplace, 0))
        mercurymass_menu.add_command(label="Insert for Mass 2", command=partial(mercuryreplace, 1))
        mercurystuff_menu.add_command(label="Radius", command=partial(mercuryreplace, 2))
        mercurystuff_menu.add_cascade(label="Orbital Radius", command=partial(mercuryreplace, 3))

        venusstuff_menu.add_cascade(label="Mass", menu=venusmass_menu)
        venusmass_menu.add_command(label="Insert for Mass 1", command=partial(venusreplace, 0))
        venusmass_menu.add_command(label="Insert for Mass 2", command=partial(venusreplace, 1))
        venusstuff_menu.add_command(label="Radius", command=partial(venusreplace, 2))
        venusstuff_menu.add_cascade(label="Orbital Radius", command=partial(venusreplace, 3))

        earthstuff_menu.add_cascade(label="Mass", menu=earthmass_menu)
        earthmass_menu.add_command(label="Insert for Mass 1", command=partial(earthreplace, 0))
        earthmass_menu.add_command(label="Insert for Mass 2", command=partial(earthreplace, 1))
        earthstuff_menu.add_command(label="Radius", command=partial(earthreplace, 2))
        earthstuff_menu.add_cascade(label="Orbital Radius", command=partial(earthreplace, 3))

        marsstuff_menu.add_cascade(label="Mass", menu=marsmass_menu)
        marsmass_menu.add_command(label="Insert for Mass 1", command=partial(marsreplace, 0))
        marsmass_menu.add_command(label="Insert for Mass 2", command=partial(marsreplace, 1))
        marsstuff_menu.add_command(label="Radius", command=partial(marsreplace, 2))
        marsstuff_menu.add_cascade(label="Orbital Radius", command=partial(marsreplace, 3))

        jupiterstuff_menu.add_cascade(label="Mass", menu=jupitermass_menu)
        jupitermass_menu.add_command(label="Insert for Mass 1", command=partial(jupiterreplace, 0))
        jupitermass_menu.add_command(label="Insert for Mass 2", command=partial(jupiterreplace, 1))
        jupiterstuff_menu.add_command(label="Radius", command=partial(jupiterreplace, 2))
        jupiterstuff_menu.add_cascade(label="Orbital Radius", command=partial(jupiterreplace, 3))

        saturnstuff_menu.add_cascade(label="Mass", menu=saturnmass_menu)
        saturnmass_menu.add_command(label="Insert for Mass 1", command=partial(saturnreplace, 0))
        saturnmass_menu.add_command(label="Insert for Mass 2", command=partial(saturnreplace, 1))
        saturnstuff_menu.add_command(label="Radius", command=partial(saturnreplace, 2))
        saturnstuff_menu.add_cascade(label="Orbital Radius", command=partial(saturnreplace, 3))

        uranusstuff_menu.add_cascade(label="Mass", menu=uranusmass_menu)
        uranusmass_menu.add_command(label="Insert for Mass 1", command=partial(uranusreplace, 0))
        uranusmass_menu.add_command(label="Insert for Mass 2", command=partial(uranusreplace, 1))
        uranusstuff_menu.add_command(label="Radius", command=partial(uranusreplace, 2))
        uranusstuff_menu.add_cascade(label="Orbital Radius", command=partial(uranusreplace, 3))

        neptunestuff_menu.add_cascade(label="Mass", menu=neptunemass_menu)
        neptunemass_menu.add_command(label="Insert for Mass 1", command=partial(neptunereplace, 0))
        neptunemass_menu.add_command(label="Insert for Mass 2", command=partial(neptunereplace, 1))
        neptunestuff_menu.add_command(label="Radius", command=partial(neptunereplace, 2))
        neptunestuff_menu.add_cascade(label="Orbital Radius", command=partial(neptunereplace, 3))

        plutostuff_menu.add_cascade(label="Mass", menu=plutomass_menu)
        plutomass_menu.add_command(label="Insert for Mass 1", command=partial(plutoreplace, 0))
        plutomass_menu.add_command(label="Insert for Mass 2", command=partial(plutoreplace, 1))
        plutostuff_menu.add_command(label="Radius", command=partial(plutoreplace, 2))
        plutostuff_menu.add_cascade(label="Orbital Radius", command=partial(plutoreplace, 3))

        root.configure(menu=menubar)


LibraryMenu(root).pack(side=TOP)

# Title Frame
title_frame = Frame(root)
title_frame.pack()

title_txt = Label(title_frame, text="Universal Gravitation", font=('Helvetica', 10, 'bold'))
title_txt.pack(pady=10, padx=10)
equation_txt = Label(title_frame, text="Fg = (G x m1 x m2) / r^2\n\nG = 6.67*10^-11\nm1 = Mass of object #1\n"
                                       "m2 = Mass of object #2\nr = Distance between centers of the masses\n"
                     , font=('Helvetica', 10))
equation_txt.pack()

# Input Frame
input_frame = Frame(root)
input_frame.pack()
mass1_var = StringVar()
mass2_var = StringVar()
radius_var = StringVar()
mass1SN_var = StringVar()
mass2SN_var = StringVar()
radiusSN_var = StringVar()
round_var = StringVar()

mass1_label = Label(input_frame, text="Mass 1 (kg)")
mass1_label.grid(row=0, column=0)
mass2_label = Label(input_frame, text="Mass 2 (kg)")
mass2_label.grid(row=1, column=0)
radius_label = Label(input_frame, text="Radius (m)")
radius_label.grid(row=2, column=0)

mass1_input = Entry(input_frame, textvariable=mass1_var)
mass1_input.grid(row=0, column=1)
mass2_input = Entry(input_frame, textvariable=mass2_var)
mass2_input.grid(row=1, column=1)
radius_input = Entry(input_frame, textvariable=radius_var)
radius_input.grid(row=2, column=1)

mass1SN_label = Label(input_frame, text="x 10^")
mass1SN_label.grid(row=0, column=2)
mass2SN_label = Label(input_frame, text="x 10^")
mass2SN_label.grid(row=1, column=2)
radiusSN_label = Label(input_frame, text="x 10^")
radiusSN_label.grid(row=2, column=2)

mass1SN_input = Entry(input_frame, textvariable=mass1SN_var, width=5)
mass1SN_input.grid(row=0, column=3)
mass2SN_input = Entry(input_frame, textvariable=mass2SN_var, width=5)
mass2SN_input.grid(row=1, column=3)
radiusSN_input = Entry(input_frame, textvariable=radiusSN_var, width=5)
radiusSN_input.grid(row=2, column=3)

round_label = Label(input_frame, text="Round Results")
round_label.grid(row=3, column=0)
round_input = Scale(input_frame, from_=0, to=10, orient=HORIZONTAL, showvalue=0, sliderlength=20, length=200, variable=round_var)
round_input.grid(row=3, column=1, columnspan=3)

# Default Values
mass1_input.insert(0, "1")
mass1SN_input.insert(0, "0")
mass2_input.insert(0, "1")
mass2SN_input.insert(0, "0")
radius_input.insert(0, "1")
radiusSN_input.insert(0, "0")
round_input.set(2)

# Result Frame
result_frame = Frame(root)
result_frame.pack()

result_label = Label(result_frame, text="NULL")
result_label.pack()

mass1_var.trace_add("write", calculate)
mass2_var.trace_add("write", calculate)
radius_var.trace_add("write", calculate)
mass1SN_var.trace_add("write", calculate)
mass2SN_var.trace_add("write", calculate)
radiusSN_var.trace_add("write", calculate)
round_var.trace_add("write", calculate)

calculate()
root.mainloop()
