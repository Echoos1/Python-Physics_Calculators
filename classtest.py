from tkinter import *
from functools import partial

root = Tk()

class LibraryMenu(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)

        def sunreplace(i):
            if i == 0:
                print("Mass 1")
            elif i == 1:
                print("Mass 2")
            elif i == 2:
                print("Radius")
            else:
                print("ERROR")

        def mercuryreplace(i):
            if i == 0:
                print("Mass 1")
            elif i == 1:
                print("Mass 2")
            elif i == 2:
                print("Radius")
            elif i == 3:
                print("Orbital Radius")
            else:
                print("ERROR")

        def venusreplace(i):
            if i == 0:
                print("Mass 1")
            elif i == 1:
                print("Mass 2")
            elif i == 2:
                print("Radius")
            elif i == 3:
                print("Orbital Radius")
            else:
                print("ERROR")

        def earthreplace(i):
            if i == 0:
                print("Mass 1")
            elif i == 1:
                print("Mass 2")
            elif i == 2:
                print("Radius")
            elif i == 3:
                print("Orbital Radius")
            else:
                print("ERROR")

        def marsreplace(i):
            if i == 0:
                print("Mass 1")
            elif i == 1:
                print("Mass 2")
            elif i == 2:
                print("Radius")
            elif i == 3:
                print("Orbital Radius")
            else:
                print("ERROR")

        def jupiterreplace(i):
            if i == 0:
                print("Mass 1")
            elif i == 1:
                print("Mass 2")
            elif i == 2:
                print("Radius")
            elif i == 3:
                print("Orbital Radius")
            else:
                print("ERROR")

        def saturnreplace(i):
            if i == 0:
                print("Mass 1")
            elif i == 1:
                print("Mass 2")
            elif i == 2:
                print("Radius")
            elif i == 3:
                print("Orbital Radius")
            else:
                print("ERROR")

        def neptunereplace(i):
            if i == 0:
                print("Mass 1")
            elif i == 1:
                print("Mass 2")
            elif i == 2:
                print("Radius")
            elif i == 3:
                print("Orbital Radius")
            else:
                print("ERROR")

        def uranusreplace(i):
            if i == 0:
                print("Mass 1")
            elif i == 1:
                print("Mass 2")
            elif i == 2:
                print("Radius")
            elif i == 3:
                print("Orbital Radius")
            else:
                print("ERROR")

        def plutoreplace(i):
            if i == 0:
                print("Mass 1")
            elif i == 1:
                print("Mass 2")
            elif i == 2:
                print("Radius")
            elif i == 3:
                print("Orbital Radius")
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
        neptunestuff_menu = Menu(self, tearoff=0)
        neptunemass_menu = Menu(self, tearoff=0)
        uranusstuff_menu = Menu(self, tearoff=0)
        uranusmass_menu = Menu(self, tearoff=0)
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
        lib_menu.add_cascade(label="Neptune", menu=neptunestuff_menu)
        lib_menu.add_cascade(label="Uranus", menu=uranusstuff_menu)
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

        neptunestuff_menu.add_cascade(label="Mass", menu=neptunemass_menu)
        neptunemass_menu.add_command(label="Insert for Mass 1", command=partial(neptunereplace, 0))
        neptunemass_menu.add_command(label="Insert for Mass 2", command=partial(neptunereplace, 1))
        neptunestuff_menu.add_command(label="Radius", command=partial(neptunereplace, 2))
        neptunestuff_menu.add_cascade(label="Orbital Radius", command=partial(neptunereplace, 3))

        uranusstuff_menu.add_cascade(label="Mass", menu=uranusmass_menu)
        uranusmass_menu.add_command(label="Insert for Mass 1", command=partial(uranusreplace, 0))
        uranusmass_menu.add_command(label="Insert for Mass 2", command=partial(uranusreplace, 1))
        uranusstuff_menu.add_command(label="Radius", command=partial(uranusreplace, 2))
        uranusstuff_menu.add_cascade(label="Orbital Radius", command=partial(uranusreplace, 3))

        plutostuff_menu.add_cascade(label="Mass", menu=plutomass_menu)
        plutomass_menu.add_command(label="Insert for Mass 1", command=partial(plutoreplace, 0))
        plutomass_menu.add_command(label="Insert for Mass 2", command=partial(plutoreplace, 1))
        plutostuff_menu.add_command(label="Radius", command=partial(plutoreplace, 2))
        plutostuff_menu.add_cascade(label="Orbital Radius", command=partial(plutoreplace, 3))

        root.configure(menu=menubar)

LibraryMenu(root).pack()
root.mainloop()
