import tkinter as tk

def change():
    name.set('Parham')

root = tk.Tk()

name = tk.StringVar()
name.set('Amirmohammad')
tk.Label(root, textvariable=name).grid(row=0, column=0)
tk.Button(root, text='', command=change).grid(row=0, column=1)

root.mainloop()
