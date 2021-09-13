from tkinter import Tk, Toplevel, Button

from random import randint

tk = Tk()
v = Toplevel(tk)
b = Button(v, text = "hola")

b.config(fg = "#%06x" % randint(0, 0xFFFFFF))
b.pack()
tk.mainloop()
