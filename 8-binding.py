from abc import abstractclassmethod
from tkinter import *


def callback(arg1, arg2, arg3, ):
    l['text'] = a.get()


root = Tk()

l = Label(root, text='Hichi')
l.pack()

a = StringVar()
a.trace("w", callback)

Entry(root, textvariable=a).pack()


root.mainloop()