import tkinter as tk

def calculate():
    pass


class Title(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)

        self.title_label = tk.Label(self, text="Coefficient of Friction", font=('Helvetica', 10, 'bold'))
        self.equation_label = tk.Label(self, text="μ = (Friction Force / Normal Force)")

        self.title_label.pack(pady=10, padx=10)
        self.equation_label.pack()
class UserInput(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)

        self.coefficient = tk.Entry(self)
        self.friction = tk.Entry(self)
        self.normal = tk.Entry(self)

        self.coefficient.pack(side=tk.TOP)
        self.friction.pack()
        self.normal.pack()
class Results(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)

        self.label = tk.Label(self, text="")

        self.label.pack()


class MainWindow(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.title = Title(self)
        self.userinput = UserInput(self)
        self.results = Results(self)

        self.title.pack(side=tk.TOP)
        self.userinput.pack()
        self.results.pack()



root = tk.Tk()
MainWindow(root).pack()
root.mainloop()
