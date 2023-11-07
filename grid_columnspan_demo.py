from tkinter import *

window = Tk()

r = Label(bg="red", width=20, height=5)
r.grid(row=1, column=0)

g = Label(bg="green", width=20, height=5)
g.grid(row=1,column=1)

b = Label(bg="blue", width=40, height=5)
# only extends width to 40 in 1st column
# b.grid(row=2, column=0)
# extend width to cover both 1st and 2nd column
b.grid(row=2, column=0, columnspan=2)

window.mainloop()
