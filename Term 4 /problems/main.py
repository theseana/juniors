from re import search
import tkinter as tk
from tkinter import ttk
from crud import crud


def register():
    cnx, cursor = crud.connect()
    if cnx != None:
        crud.create(
        cnx, cursor, 
        first_name.get().lower(), 
        last_name.get().lower(),
        phone.get(), 
        sex.get(), 
        )    


def check():
    cnx, cursor = crud.connect()
    if cnx != None:
        athletes = crud.read(cnx, cursor)
        tree.delete(*tree.get_children())
        for ahtlete in athletes:
            tree.insert("", 0, text="", values=(ahtlete[1], ahtlete[2], ahtlete[3], ahtlete[4]))


def get():
    cnx, cursor = crud.connect()
    if cnx != None:
        athlete = crud.get_one(cnx, cursor, id_search.get())
        if athlete != None:
            first_name_u.set(athlete[1])
            last_name_u.set(athlete[2])
            phone_u.set(athlete[3])
            sex_u.set(athlete[4])


def update():
    cnx, cursor = crud.connect()
    if cnx != None:
        crud.update(
        cnx, cursor, 
        first_name_u.get().lower(), 
        last_name_u.get().lower(),
        phone_u.get(), 
        sex_u.get(),
        id_search.get(),
        )    


def delete():
    cnx, cursor = crud.connect()
    if cnx != None:
        crud.delete(
        cnx, cursor, 
        id_delete.get(),
        )


root = tk.Tk()

note = ttk.Notebook()
note.grid(row=0, column=0)
c = tk.Frame()
r = tk.Frame()
u = tk.Frame()
d = tk.Frame()
note.add(c, text='Create')
note.add(r, text='Read')
note.add(u, text='Update')
note.add(d, text='Delete')
# ##############################################################
tk.Label(c, text="First Name:").grid(row=0, column=0)
first_name = tk.StringVar()
tk.Entry(c, textvariable=first_name).grid(row=0, column=1)

tk.Label(c, text="Last Name:").grid(row=1, column=0)
last_name = tk.StringVar()
tk.Entry(c, textvariable=last_name).grid(row=1, column=1)

tk.Label(c, text="Phone:").grid(row=2, column=0)
phone = tk.StringVar()
tk.Entry(c, textvariable=phone).grid(row=2, column=1)

tk.Label(c, text="Sex:").grid(row=3, column=0)
sex = tk.StringVar()
sex.set('f')
options = ['m', 'f', 'others']
tk.OptionMenu(c, sex, *options).grid(row=3, column=1, sticky=tk.W+tk.E)
tk.Button(c,
    text='Register',
    command=register).grid(row=4, column=0, columnspan=2, sticky=tk.W+tk.E)
# ##############################################################
tk.Button(r,
    text='Check',
    command=check).grid(row=0, column=0, columnspan=1)

tree = ttk.Treeview(r, selectmode ='browse')

verscrlbar = ttk.Scrollbar(r, orient ="vertical", command=tree.yview) 
verscrlbar.grid(row=1, column=3) 
tree.configure(xscrollcommand=verscrlbar.set) 

tree["columns"]=("one","two","three", "four")
tree.column("#0", width=1, stretch=tk.NO)
tree.column("one", width=70, minwidth=150, stretch=tk.NO)
tree.column("two", width=70)
tree.column("three", width=80, minwidth=50, stretch=tk.NO)
tree.column("four", width=50, minwidth=50, stretch=tk.NO)
tree.heading("#0",text="ID",anchor=tk.W)
tree.heading("one", text="FirstName",anchor=tk.W)
tree.heading("two", text="LastName",anchor=tk.W)
tree.heading("three", text="Phone",anchor=tk.W)
tree.heading("four", text="Sex",anchor=tk.W)
tree.grid(row=1, column=0, columnspan=3)
# ##############################################################
tk.Label(u, text="ID:").grid(row=0, column=0)
id_search = tk.StringVar()
tk.Entry(u, textvariable=id_search).grid(row=0, column=1)

tk.Button(u,
    text='Get',
    command=get).grid(row=0, column=2)

tk.Label(u, text="First Name:").grid(row=1, column=0)
first_name_u = tk.StringVar()
tk.Entry(u, textvariable=first_name_u).grid(row=1, column=1)

tk.Label(u, text="Last Name:").grid(row=2, column=0)
last_name_u = tk.StringVar()
tk.Entry(u, textvariable=last_name_u).grid(row=2, column=1)

tk.Label(u, text="Phone:").grid(row=3, column=0)
phone_u = tk.StringVar()
tk.Entry(u, textvariable=phone_u).grid(row=3, column=1)

tk.Label(u, text="Sex:").grid(row=4, column=0)
sex_u = tk.StringVar()
sex_u.set('f')
options = ['m', 'f', 'others']
tk.OptionMenu(u, sex_u, *options).grid(row=4, column=1, sticky=tk.W+tk.E)
tk.Button(u,
    text='Update',
    command=update).grid(row=5, column=0, columnspan=2)
# ##############################################################
tk.Label(d, text="ID:").grid(row=0, column=0)
id_delete = tk.StringVar()
tk.Entry(d, textvariable=id_delete).grid(row=0, column=1)

tk.Button(d,
    text='Delete',
    command=delete).grid(row=0, column=2)

root.mainloop()