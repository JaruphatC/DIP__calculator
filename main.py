import tkinter as tk
class Myclaculator:
    def __init__(self):
        
        self.root = tk.Tk()

        self.root.geometry("900x900")
        self.root.title("My calculator")

        self.label = tk.Label(self.root, text="Calculator", font=('Comic Sans MS', 80))
        self.label.pack()

        self.button = tk.Button(self.root, text="1", height=1, width=3, font=('Comic Sans MS', 15))
        self.button.place(x=850, y=200)

        self.button = tk.Button(self.root, text="2", height=1, width=3, font=('Comic Sans MS', 15))
        self.button.place(x=900, y=200)

        self.button = tk.Button(self.root, text="3", height=1, width=3, font=('Comic Sans MS', 15))
        self.button.place(x=950, y=200)

        self.button = tk.Button(self.root, text="4", height=1, width=3, font=('Comic Sans MS', 15))
        self.button.place(x=850, y=250)

        self.button = tk.Button(self.root, text="5", height=1, width=3, font=('Comic Sans MS', 15))
        self.button.place(x=900, y=250)

        self.button = tk.Button(self.root, text="6", height=1, width=3, font=('Comic Sans MS', 15))
        self.button.place(x=950, y=250)

        self.button = tk.Button(self.root, text="7", height=1, width=3, font=('Comic Sans MS', 15))
        self.button.place(x=850, y=300)

        self.button = tk.Button(self.root, text="8", height=1, width=3, font=('Comic Sans MS', 15))
        self.button.place(x=900, y=300)

        self.button = tk.Button(self.root, text="9", height=1, width=3, font=('Comic Sans MS', 15))
        self.button.place(x=950, y=300)

        self.button = tk.Button(self.root, text="0", height=1, width=3, font=('Comic Sans MS', 15))
        self.button.place(x=850, y=350)

        self.button = tk.Button(self.root, text="00", height=1, width=3, font=('Comic Sans MS', 15))
        self.button.place(x=900, y=350)

        self.button = tk.Button(self.root, text="+", height=1, width=3, font=('Comic Sans MS', 15))
        self.button.place(x=1000, y=200)

        self.button = tk.Button(self.root, text="-", height=1, width=3, font=('Comic Sans MS', 15))
        self.button.place(x=1000, y=250)

        self.button = tk.Button(self.root, text="x", height=1, width=3, font=('Comic Sans MS', 15))
        self.button.place(x=1000, y=300)

        self.button = tk.Button(self.root, text="%", height=1, width=3, font=('Comic Sans MS', 15))
        self.button.place(x=1000, y=350)
        
        self.button = tk.Button(self.root, text="=", height=1, width=3, font=('Comic Sans MS', 15))
        self.button.place(x=950, y=350)



        self.root.mainloop()

Myclaculator()






