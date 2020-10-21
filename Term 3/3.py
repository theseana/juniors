import tkinter as tk
from threading import Thread
from time import sleep


def stop(side):
    global Left
    if side == 'left':
        Left = True
    else:
        Left = False


def start(val):
    timer['left'] = timer['right'] = val
    while True:
        if timer['left'] == 0 or timer['right'] == 0:
            break
        sleep(1)
        if Left:
            timer['right'] -= 1
            m, s = divmod(timer['right'], 60)

            r_timer.set('%02d:%02d' % (m, s))
        else:
            timer['left'] -= 1
            m, s = divmod(timer['left'], 60)

            l_timer.set('%02d:%02d' % (m, s))


#################################################
def begin():
    value = time_value.get()

    m, s = divmod(value, 60)

    r_timer.set('%02d:%02d' % (m, s))
    l_timer.set('%02d:%02d' % (m, s))

    thread1 = Thread(target=start, args=(value,))
    thread1.start()

#################################################

l_cnf = {'bg': '#7C4DFF', 'fg': '#FFD600'}
tk_cnf = {'bg': l_cnf['bg']}

root = tk.Tk()
root.resizable(0, 0)
root.title('Digital Chess Timer')
root.config(cnf=tk_cnf)

timer = {}
Left = False

tk.Label(root,
         cnf=l_cnf,
         text='Left Player',
         font=('times', 20, 'italic')).grid(row=0, column=0)
tk.Label(root,
         cnf=l_cnf,
         text='Right Player',
         font=('times', 20, 'italic')).grid(row=0, column=1)
###################################################

# Timer#############################################
l_timer = tk.StringVar()
l_timer.set('00:00')
tk.Label(root,
         cnf=l_cnf,
         textvariable=l_timer,
         font=('courier', 20)).grid(row=1, column=0)
r_timer = tk.StringVar()
r_timer.set('00:00')
tk.Label(root,
         cnf=l_cnf,
         textvariable=r_timer,
         font=('courier', 20)).grid(row=1, column=1)
###################################################

# Buttons #########################################
b_cnf = {'bg': '#311B92',
         'activebackground': '#7C4DFF',
         'highlightbackground': '#7C4DFF'}
tk.Button(root,
          cnf=b_cnf,
          text='Stop',
          command=lambda: stop('left'),
          font=('times', 20)).grid(row=2, column=0, sticky=tk.W + tk.E)
tk.Button(root,
          cnf=b_cnf,
          text='Stop',
          command=lambda: stop('right'),
          font=('times', 20)).grid(row=2, column=1, sticky=tk.W + tk.E)
time_value = tk.IntVar()
tk.Entry(root,
         textvariable=time_value,
         font=('times', 20)).grid(row=3, column=0, columnspan=2)
tk.Button(root,
          cnf=b_cnf,
          text='Start',
          command=begin,
          font=('times', 20)).grid(row=4, column=0, columnspan=2, sticky=tk.W + tk.E)
tk.Button(root,
          cnf=b_cnf,
          text='Cancel',
          command=root.destroy,
          font=('times', 20)).grid(row=5, column=0, columnspan=2, sticky=tk.W + tk.E)
###################################################
root.mainloop()
