import tkinter as tk


root = tk.Tk()

l1 = tk.Label(root, text='L1', bg='red', font=('times', 20))
l1.grid(row=0, column=0)


l2 = tk.Label(root, text='L2', bg='yellow', font=('times', 20))
l2.grid(row=0, column=1, columnspan=3, sticky=tk.W+tk.E)

l3 = tk.Label(root, text='L3', bg='pink', font=('times', 20))
l3.grid(row=1, column=0)

l4 = tk.Label(root, text='L4', bg='green', font=('times', 20))
l4.grid(row=1, column=1, rowspan=2, sticky=tk.S)

l5 = tk.Label(root, text='L5', bg='red', font=('times', 20))
l5.grid(row=1, column=2, rowspan=3, sticky=tk.N+tk.S)

l6 = tk.Label(root, text='L6', bg='blue', font=('times', 20))
l6.grid(row=1, column=3, rowspan=3, sticky=tk.N+tk.S)

l7 = tk.Label(root, text='L7', bg='yellow', font=('times', 20))
l7.grid(row=2, column=0, rowspan=2, sticky=tk.S)

l8 = tk.Label(root, text='L8', bg='white', font=('times', 20))
l8.grid(row=3, column=1)

root.mainloop()
