from tkinter import Tk, Button

def nBoton(tk, text):
    b = Button(tk, text = text)
    b.pack()

tk = Tk()

nBoton(tk, "1")
nBoton(tk, "2")

tk.mainloop()
