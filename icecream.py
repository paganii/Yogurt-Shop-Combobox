from tkinter import *

screen=Tk()
screen.title("Screen")
screen.geometry("600x600")
screen.config(background="yellow")
Label(screen, text="Choose your ice cream", font="Arial 35").pack()

# frame
frame = Frame(screen, bg="pink", width=200, height=200)
frame.pack(pady=20, padx=20)

scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=X)
lb=Listbox(frame, width=50, height=10)
lb.pack(side=LEFT)

scrollbar.config(command=lb.yview)
flavours = ["Apple", "Banana", "Cherry", "Date", "Elderberry",
    "Fig", "Grapes", "Honeydew", "Indian Fig", "Jackfruit",
    "Kiwi", "Lemon", "Mango", "Nectarine", "Orange",
    "Papaya", "Quince", "Raspberry", "Strawberry", "Tomato"]
for i in flavours:
    lb.insert(END, i)
screen.mainloop()