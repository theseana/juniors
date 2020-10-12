import tkinter as tk
from datetime import datetime


def turn():
    global n
    n += 1
    numbers.append(n + 1)
    d = datetime.now()
    l1.config(text=d.strftime("%B/%d/%Y"))
    a1.config(text=d.strftime("%-H:%-M:%-S"))
    c1.config(text=d.strftime("%A"))
    e1.config(text='Your Turn:' + str(numbers[-1]))
    e2.config(text='Left:' + str(len(numbers) - 1))
    line = '{},{},{}\n'.format(numbers[-1],
                               d.strftime("%-H:%-M:%-S"),
                               d.strftime("%d-%-m-%Y"))
    with open('turns.csv', 'a') as file:
        file.write(line)


def append_csv(number, operator):
    d = datetime.now()
    line = '{},{},{},Operator{}\n'.format(number,
                                          d.strftime("%-H:%-M:%-S"),
                                          d.strftime("%d-%-m-%Y"),
                                          operator)
    with open('operators.csv', 'a') as file:
        file.write(line)


def op1():
    if numbers:
        number = numbers.pop(0)
        lo1.config(text=number)
        append_csv(number, 1)


def op2():
    if numbers:
        number = numbers.pop(0)
        lo2.config(text=number)
        append_csv(number, 2)


def op3():
    if numbers:
        number = numbers.pop(0)
        lo3.config(text=number)
        append_csv(number, 3)


root = tk.Tk()

n = -1
numbers = []

l1 = tk.Label(root, text='')
l1.grid(row=0, column=0)
a1 = tk.Label(root, text='')
a1.grid(row=1, column=0)
c1 = tk.Label(root, text='')
c1.grid(row=2, column=0)
e1 = tk.Label(root, text='')
e1.grid(row=3, column=0)
e2 = tk.Label(root, text='')
e2.grid(row=4, column=0)

b1 = tk.Button(root, text='Get Turn!', command=turn)
b1.grid(row=5, column=0)

tp = tk.Toplevel(root)

o1 = tk.Button(tp, text='Operator1', command=op1)
o1.grid(row=0, column=0)
o2 = tk.Button(tp, text='Operator2', command=op2)
o2.grid(row=0, column=1)
o3 = tk.Button(tp, text='Operator3', command=op3)
o3.grid(row=0, column=2)

lo1 = tk.Label(tp, text='--')
lo1.grid(row=1, column=0)
lo2 = tk.Label(tp, text='--')
lo2.grid(row=1, column=1)
lo3 = tk.Label(tp, text='--')
lo3.grid(row=1, column=2)

root.mainloop()
