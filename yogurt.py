from tkinter import *
from tkinter import ttk
screen=Tk()
screen.title("Yogurt Shop")
screen.config(background="ivory")
screen.geometry("600x600")

titlee = Label(screen, text="Yogurt Shop").place(x=250, y=50)
Label(screen, text="Choose your favorite base.").place(x=90, y=95)
basevariable=StringVar()
basechoice = ttk.Combobox(screen, textvariable=basevariable,state="readonly", values=["Original White", "Black Sakura", "Sugar Pink", "Vanilla Plum", "Blue Cane"])
basechoice.place(x=50, y=120)
basechoice.current(0)
screen.mainloop()