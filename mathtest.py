from tkinter import *

root = Tk()

def dostuff():
    print("did stuff")

menubar = Menu(tearoff=0)

sun_menu = Menu(tearoff=0)
sunstuff_menu = Menu(tearoff=0)
sunmass_menu = Menu(tearoff=0)
sunrad_menu = Menu(tearoff=0)
sunorb_menu = Menu(tearoff=0)

menubar.add_cascade(label="Library", menu=sun_menu)

sun_menu.add_cascade(label="Sun", menu=sunstuff_menu)
sunstuff_menu.add_cascade(label="Mass", menu=sunmass_menu)
sunmass_menu.add_command(label="Insert for Mass 1", command=dostuff)
sunmass_menu.add_command(label="Insert for Mass 2",command=dostuff)
sunstuff_menu.add_command(label="Radius", command=dostuff)
sunstuff_menu.add_cascade(label="Orbital Radius", command=dostuff)





root.configure(menu=menubar)
root.mainloop()