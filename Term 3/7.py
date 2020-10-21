from time import sleep
import tkinter as tk
from tkinter import Frame
import tkinter.ttk as ttk
from threading import Thread

from conf import *


def time_format(seconds):
    h = int(seconds / 3600)
    temp = seconds % 3600
    m = temp / 60
    s = temp % 60
    return '%02d:%02d:%02d'%(h, m, s)

def counter(seconds, var, button):
    button.config(state=tk.DISABLED)
    while seconds:
        sleep(1)
        seconds -= 1
        var.set(time_format(seconds))
    button.config(state=tk.ACTIVE)

def start(number):
    if number == 1:
        seconds1 = int(h_p_1.get()) * 3600 + int(m_p_1.get()) * 60 + int(s_p_1.get())
        th1 = Thread(target=counter, args=(seconds1, t1, b1))
        th1.start()
    elif number == 2:
        seconds2 = int(h_p_2.get()) * 3600 + int(m_p_2.get()) * 60 + int(s_p_2.get())
        th2 = Thread(target=counter, args=(seconds2, t2, b2))
        th2.start()
    else:
        seconds3 = int(h_p_3.get()) * 3600 + int(m_p_3.get()) * 60 + int(s_p_3.get())
        th3 = Thread(target=counter, args=(seconds3, t3, b3))
        th3.start()

def callback1(arg1, arg2, arg3):
    p1.set(n_p_1.get())
 
def callback2(arg1, arg2, arg3):
    p2.set(n_p_2.get())
   
def callback3(arg1, arg2, arg3):
    p3.set(n_p_3.get())

def callback_t_1(arg1, arg2, arg3):
    t1.set('%02d:%02d:%02d'%(int(h_p_1.get()), int(m_p_1.get()), int(s_p_1.get())))

def callback_t_2(arg1, arg2, arg3):
    t2.set('%02d:%02d:%02d'%(int(h_p_2.get()), int(m_p_2.get()), int(s_p_2.get())))

def callback_t_3(arg1, arg2, arg3):
    t3.set('%02d:%02d:%02d'%(int(h_p_3.get()), int(m_p_3.get()), int(s_p_3.get())))
        
root = tk.Tk()

note = ttk.Notebook()
note.grid(row=0, column=0)

timer = tk.Frame(bg='#efd6ac')
patient = tk.Frame(bg='#efd6ac')

note.add(timer, text='Timer')
note.add(patient, text='Patient')

# ############### Timer First Row ############## #
p1 = tk.StringVar()
p1.set('Patient1')
tk.Label(timer, textvariable=p1, cnf=label_name).grid(row=0, column=0, pady=10)
p2 = tk.StringVar()
p2.set('Patient2')
tk.Label(timer, textvariable=p2, cnf=label_name).grid(row=0, column=1, pady=10)
p3 = tk.StringVar()
p3.set('Patient3')
tk.Label(timer, textvariable=p3, cnf=label_name).grid(row=0, column=2, pady=10)
# ############## Timer Second Row ############## #
t1 = tk.StringVar()
t1.set('00:00:00')
tk.Label(timer, textvariable=t1, cnf=label_time).grid(row=1, column=0)
t2 = tk.StringVar()
t2.set('00:00:00')
tk.Label(timer, textvariable=t2, cnf=label_time).grid(row=1, column=1)
t3 = tk.StringVar()
t3.set('00:00:00')
tk.Label(timer, textvariable=t3, cnf=label_time).grid(row=1, column=2)
# ########### Timer Third Row Buttons ########## #
b1 = tk.Button(timer, text='Start', cnf=button_start, command=lambda: start(1))
b1.grid(row=2, column=0)
b2 = tk.Button(timer, text='Start', cnf=button_start, command=lambda: start(2))
b2.grid(row=2, column=1)
b3 = tk.Button(timer, text='Start', cnf=button_start, command=lambda: start(3))
b3.grid(row=2, column=2)
# ######## Timer Last Row Cancel Button ######## #
tk.Button(timer, text='Cancel', cnf=button_cancel ,command=root.destroy).grid(row=3, column=0, columnspan=3, sticky=tk.E+tk.W)
# ############ Patient 1 Name Timer ############ #
patient1 = tk.LabelFrame(patient, text='Patient1')
patient1.grid(row=0, column=0, padx=10)

tk.Label(patient1, text='Name').grid(row=0, column=0)
tk.Label(patient1, text='Timer').grid(row=1, column=0)
# ------------------Name--------------------- #
n_p_1 = tk.StringVar()
n_p_1.trace('w', callback1)
tk.Entry(patient1, textvariable=n_p_1).grid(row=0, column=1)
# ------------------Timer-------------------- #
h_p_1 = tk.StringVar()
h_p_1.set('12')
m_p_1 = tk.StringVar()
m_p_1.set('30')
s_p_1 = tk.StringVar()
s_p_1.set('30')
f1 = tk.Frame(patient1)
f1.grid(row=1, column=1)
tk.Spinbox(f1, from_=0, to=23, wrap=True, textvariable=h_p_1, width=2,
           state="readonly").grid(row=0, column=0)
tk.Spinbox(f1, from_=0, to=59, wrap=True, textvariable=m_p_1, width=2,
           state="readonly").grid(row=0, column=1)
tk.Spinbox(f1, from_=0, to=59, wrap=True, textvariable=s_p_1, width=2,
           state="readonly").grid(row=0, column=2)
# ############ Patient 2 Name Timer ############ #
patient2 = tk.LabelFrame(patient, text='Patient2')
patient2.grid(row=1, column=0, padx=10)

tk.Label(patient2, text='Name').grid(row=0, column=0)
tk.Label(patient2, text='Timer').grid(row=1, column=0)
# ------------------Name--------------------- #
n_p_2 = tk.StringVar()
n_p_2.trace('w', callback2)
tk.Entry(patient2, textvariable=n_p_2).grid(row=0, column=1)
# ------------------Timer-------------------- #
h_p_2 = tk.StringVar()
h_p_2.set('12')
m_p_2 = tk.StringVar()
m_p_2.set('30')
s_p_2 = tk.StringVar()
s_p_2.set('30')
f2 = tk.Frame(patient2)
f2.grid(row=1, column=1)
tk.Spinbox(f2, from_=0, to=23, wrap=True, textvariable=h_p_2, width=2,
           state="readonly").grid(row=0, column=0)
tk.Spinbox(f2,
           from_=0,
           to=59,
           wrap=True,
           textvariable=m_p_2,
           width=2,
           state="readonly").grid(row=0, column=1)
tk.Spinbox(f2,
           from_=0,
           to=59,
           wrap=True,
           textvariable=s_p_2,
           width=2,
           state="readonly").grid(row=0, column=2)
# ############ Patient 3 Name Timer ############ #
patient3 = tk.LabelFrame(patient, text='Patient3')
patient3.grid(row=2, column=0, padx=10)

tk.Label(patient3, text='Name').grid(row=0, column=0)
tk.Label(patient3, text='Timer').grid(row=1, column=0)
# ------------------Name--------------------- #
n_p_3 = tk.StringVar()
n_p_3.trace('w', callback3)
tk.Entry(patient3, textvariable=n_p_3).grid(row=0, column=1)
# ------------------Timer-------------------- #
h_p_3 = tk.StringVar()
h_p_3.set('12')
m_p_3 = tk.StringVar()
m_p_3.set('30')
s_p_3 = tk.StringVar()
s_p_3.set('30')
f3 = tk.Frame(patient3)
f3.grid(row=1, column=1)
tk.Spinbox(f3,
           from_=0,
           to=23,
           wrap=True,
           textvariable=h_p_3,
           width=2,
           state="readonly").grid(row=0, column=0)
tk.Spinbox(f3,
           from_=0,
           to=59,
           wrap=True,
           textvariable=m_p_3,
           width=2,
           state="readonly").grid(row=0, column=1)
tk.Spinbox(f3,
           from_=0,
           to=59,
           wrap=True,
           textvariable=s_p_3,
           width=2,
           state="readonly").grid(row=0, column=2)
# --------------- Timer Callbacks -------------- #
h_p_1.trace('w', callback_t_1)
m_p_1.trace('w', callback_t_1)
s_p_1.trace('w', callback_t_1)
h_p_2.trace('w', callback_t_2)
m_p_2.trace('w', callback_t_2)
s_p_2.trace('w', callback_t_2)
h_p_3.trace('w', callback_t_3)
m_p_3.trace('w', callback_t_3)
s_p_3.trace('w', callback_t_3)
root.mainloop()