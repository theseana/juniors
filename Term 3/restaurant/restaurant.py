import pandas as pd 

import tkinter as tk
from tkinter import PhotoImage
import tkinter.ttk as ttk

from config import *


def cnt(sign, j):
    j = int(j)
    if sign == '+':
        i[j]['count'] += 1
    else:
        if i[j]['count']:
            i[j]['count'] -= 1
        else:
            pass
    count[j].set(i[j]['count'])


def cntd(sign, j):
    j = int(j)
    if sign == '+':
        d[j]['count'] += 1
    else:
        if d[j]['count']:
            d[j]['count'] -= 1
        else:
            pass
    countd[j].set(d[j]['count'])


def rec():
    df_d = pd.DataFrame(d).T
    df_d = df_d[df_d["count"] != 0].set_index('name')
    df_f = pd.DataFrame(i).T[["name", "price", "count"]]
    df_f = df_f[df_f["count"] != 0].set_index('name')
    frames = [df_d, df_f]
    df = pd.concat(frames)
    df['fee'] = df['price'] * df['count']
    
    for index, row in df.iterrows():
        # print("index>>>>",index,"\nrow", row[0], row[1], row[2]) 
        tree.insert("", 0, text="", values=(index, row[0], row[1], row[2]))
    
    tree.insert("", 100, text="", values=("", "", "total:", df['fee'].sum() ))

    
# $$$$$$$$$$$$$$$$$$$ Food Information $$$$$$$$$$$$$$$$$$$ #
i = {
    0: {'name': 'BaqaliQatoq',
          'rating': 5,
          'review': 47, 
          'price': 1.5,
          'count': 0,
          'des':'This is Iranian Food, which most used in north of IRAN Elit reprehen derit exce pteur dolor labore ipsum veniam exercitation deserunt.',
          'img': 'images/baqali.gif'},
    1: {'name': 'SabziQormeh',
          'rating': 4,
          'review': 72,
          'price': 1,
          'count': 0,
          'des':'This is Iranian Food, which most used in north of IRAN Elit reprehen derit exce pteur dolor labore ipsum veniam exercitation deserunt.',
          'img': 'images/baqali1.gif'}
}

d = {
    0: {'name': 'Cola',
          'price': 1.5,
          'count': 0},
    1: {'name': 'Pepsi',
          'price': 1,
          'count': 0},
    2: {'name': 'Fanta',
          'price': 1.5,
          'count': 0},
    3: {'name': 'Water',
          'price': 1,
          'count': 0},
    4: {'name': 'Lemonade',
          'price': 1.5,
          'count': 0},
    5: {'name': 'Mojito',
          'price': 1,
          'count': 0}
}

countd = {}
count = {}
image = {}
img = {}
# -------------------------------------------------------- #

root = tk.Tk()
root.title('Restauran Menu System')
note = ttk.Notebook()
note.grid(row=0 , column=0)
# ################ NoteBook Tabs ############### #
food = tk.Frame()
drink = tk.Frame(bg='#0377fc')
reciept = tk.Frame()
# ---------------------------------------------- #
note.add(food, text='Foods')
note.add(drink, text='Drinks')
note.add(reciept, text='Recipt')
# ################## Food Tab ################## #

for j in range(len(i)):
    f1 = tk.Frame(food,bg='#ffc107')
    f1.grid(row=j, column=0)

    name = i[j]['name']
    tk.Label(f1,
        text=name,
        width=10,
        cnf=label_cnf,
        anchor='w').grid(row=0, column=0, sticky=tk.W)

    rating = i[j]['rating'] * '★' + '(' + str(i[j]['review']) +')'
    tk.Label(f1,
        text=rating,
        font='fixedsys',
        anchor='nw').grid(row=1, column=0, sticky="nw", padx=10, pady=5)

    f1_5 = tk.Frame(f1, bg='#ffc107')
    f1_5.grid(row=1, column=1)

    image[j] = PhotoImage(file='cart.gif').subsample(7)
    tk.Label(f1_5, image=image[j], bg='#ffc107', fg='#ffffff').grid(row=0, column=0)
    
    count[j] = tk.StringVar()
    count[j].set(i[j]['count'])
    tk.Label(f1_5, textvariable=count[j], font=('times', 15), bg='#ffc107').grid(row=0, column=1, sticky=tk.S)
    tk.Button(f1_5, text='+', command=lambda x=str(j): cnt('+', x) ).grid(row=0, column=2)
    tk.Button(f1_5, text='-', command=lambda y=str(j): cnt('-', y) ).grid(row=0, column=3)
 
    des = i[j]['des']
    tk.Message(f1,
        text=des,
        font='fixedsys',
        width=200).grid(row=2, column=0, columnspan=2, pady=5)

    price = str(i[j]['price']) + '$' 
    tk.Label(f1,
        text=price,
        font='fixedsys').grid(row=0, column=1)

    img[j] = PhotoImage(file=i[j]['img'])
    tk.Label(f1,
        image=img[j],
        borderwidth=4,
        relief="sunken",
        highlightcolor="red").grid(row=0, column=2, rowspan=4, padx=5, stick=tk.S, pady=5)

# ################## Drink Tab ################## #

for l in range(len(d)):
    f1 = tk.Frame(drink,bg='#0377fc')
    f1.grid(row=l, column=0, padx=120, pady=5)

    name = d[l]['name']
    tk.Label(f1,
        text=name,
        width=10,
        bg='#0377fc',
        font=('fixedsys', 20),
        anchor='w').grid(row=0, column=0, sticky=tk.W)


    f1_5 = tk.Frame(f1, bg='#ffc107')
    f1_5.grid(row=1, column=1)

    image[l] = PhotoImage(file='cartd.gif').subsample(7)
    tk.Label(f1_5, image=image[l], bg='#ffc107', fg='#ffffff').grid(row=0, column=0)
    
    countd[l] = tk.StringVar()
    countd[l].set(d[l]['count'])
    
    tk.Label(f1_5, textvariable=countd[l], font=('times', 15), bg='#ffc107').grid(row=0, column=1, sticky=tk.S)
    tk.Button(f1_5, text='+', command=lambda x=str(l): cntd('+', x) ).grid(row=0, column=2)
    tk.Button(f1_5, text='-', command=lambda x=str(l): cntd('-', x) ).grid(row=0, column=3)
 
    price = str(d[l]['price']) + '$' 
    tk.Label(f1,
             bg='#0377fc',
            text=price,
            font='fixedsys').grid(row=0, column=1)
# ################## Recitp Tab ################## #
tk.Button(reciept, text='Confirm', command=rec).grid(row=0, column=0)
tree = ttk.Treeview(reciept)
tree.grid(row=1, column=0, columnspan=3)
tree["columns"]=("one","two","three", "four")
tree.column("#0", width=1, stretch=tk.NO)
tree.column("one", width=150, minwidth=150, stretch=tk.NO)
tree.column("two", width=70)
tree.column("three", width=80, minwidth=50, stretch=tk.NO)
tree.column("four", width=80, minwidth=50, stretch=tk.NO)

tree.heading("#0",text="ID",anchor=tk.W)
tree.heading("one", text="Name",anchor=tk.W)
tree.heading("two", text="Fee",anchor=tk.W)
tree.heading("three", text="Count",anchor=tk.W)
tree.heading("four", text="Price",anchor=tk.W)

root.mainloop()