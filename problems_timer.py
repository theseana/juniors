import tkinter as tk


def c():
    l.set(e.get())


root = tk.Tk()

l = tk.StringVar()
l.set('Problem')
tk.Label(root, textvariable=l).grid(row=0, column=1)

e = tk.StringVar()
e.set('')
tk.Entry(root, textvariable=e).grid(row=0, column=0)


b = tk.Button(root, text='Check!', command=c)
b.grid(row=1, column=0)

root.mainloop()