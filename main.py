import tkinter as tk
class Myclaculator:
    def __init__(self):
        
        self.root = tk.Tk()

        self.root.geometry("900x900")
        self.root.title("My calculator")

        self.label = tk.Label(self.root, text="Calculator", font=('Comic Sans MS', 80))
        self.label.pack()

        self.button = tk.Button(self.root, text="1", font=('Comic Sans MS', 15))
        self.button.place(x=900, y=150)

        self.button = tk.Button(self.root, text="+", font=('Comic Sans MS', 15))
        self.button.place(x=900, y=200)

        self.button = tk.Button(self.root, text="-", font=('Comic Sans MS', 15))
        self.button.place(x=900, y=250)

        self.button = tk.Button(self.root, text="x", font=('Comic Sans MS', 15))
        self.button.place(x=900, y=300)

        self.button = tk.Button(self.root, text="//", font=('Comic Sans MS', 15))
        self.button.place(x=900, y=350)

        self.button = tk.Button(self.root, text="**", font=('Comic Sans MS', 15))
        self.button.place(x=900, y=400)

        self.root.mainloop()

Myclaculator()






