import tkinter as tk
import tkinter.ttk as ttk
from tkinter import Toplevel, messagebox
import hashlib
import json
import datetime
import random


def change():
    def change_pass():
        new_pass = new.get()
        new_pass1 = new1.get()
        if new_pass == new_pass1:
            all = read_json('names.json')
            if all[index]['password'] == to_sha1(old.get()):
                all[index]['password'] = to_sha1(new.get())
                write_json('names.json', all)

            else:
                messagebox.showerror("Not Valid", "Enter Correct Old-Password")
        else:
            messagebox.showerror("Not the same", "Retype same Password")

    def chg_close():
        chg.destroy()
        top.deiconify()
    top.withdraw()
    chg = Toplevel()
    tk.Label(chg, text="Old Password:").grid(row=0, column=0)
    old = tk.StringVar()
    tk.Entry(chg, show='*', textvariable=old).grid(row=0, column=1)
    tk.Label(chg, text="New Password:").grid(row=1, column=0)
    new = tk.StringVar()
    tk.Entry(chg, show='*', textvariable=new).grid(row=1, column=1)
    tk.Label(chg, text="New Password:").grid(row=2, column=0)
    new1 = tk.StringVar()
    tk.Entry(chg, show='*', textvariable=new1).grid(row=2, column=1)
    tk.Button(chg, text="Change", command=change_pass).grid(row=3, column=0, columnspan=2, sticky=tk.W+tk.E)
    tk.Button(chg, text="Close", command=chg_close).grid(row=4, column=0, columnspan=2, sticky=tk.W+tk.E)

def balance():
    def bln_close():
        bln.destroy()
        top.deiconify()

    all = read_json('names.json')
    top.withdraw()
    bln = Toplevel()
    string= f"""
Name    : {all[index]['username']}
Balance : {all[index]['balance']}
"""
    tk.Message(bln, text=string).grid(row=0, column=0)
    tk.Button(bln,
              text='Close',
              command=bln_close
    ).grid(row=2, column=0, columnspan=2)


def deposite():
    def deposite_money():
        all = read_json('names.json')
        if all[index]['balance'] > deposite_amount.get():

            all[index]['balance'] -= deposite_amount.get()
            write_json('names.json', all)

            deposite_transaction['username'] = all[index]['username']
            deposite_transaction['balance'] = all[index]['balance']
            deposite_transaction['card_number'] = all[index]['card_number']
            deposite_transaction['amount'] = deposite_amount.get()
            deposite_transaction['created_at'] = get_datetime()
            
            all_tra = read_json('transactions.json')
            all_tra.append(deposite_transaction)
            write_json('transactions.json', all_tra)

        else:
            messagebox.showerror("Less Money", "Not Enough MOney")

    def deposite_destroy():
        dps.destroy()
        top.deiconify()

    top.withdraw()
    dps = tk.Toplevel()
    tk.Label(dps, text='Amount').grid(row=0, column=0)
    deposite_amount = tk.IntVar()
    tk.Entry(dps, textvariable=deposite_amount).grid(row=0, column=1)
    tk.Button(dps, text='Deposite', command=deposite_money).grid(row=1, column=0, columnspan=2)
    tk.Button(dps, text='Close', command=deposite_destroy).grid(row=2, column=0, columnspan=2)


def find_destination(destination_card):
    all = read_json('names.json')
    for person in all:
        if person['card_number'] == destination_card:
            return all.index(person)
    return None


def transfer():
    def transfer_confrimation(index, destination_index, confirmation):
        all = read_json('names.json')
        all[index]['balance'] -= destination_amount.get()
        all[destination_index]['balance'] += destination_amount.get()
        write_json('names.json', all)
        
        transfer_transaction['username'] = all[index]['username']
        transfer_transaction['balance'] = all[index]['balance']
        transfer_transaction['from'] = all[index]['card_number']
        transfer_transaction['to'] = all[destination_index]['card_number']
        transfer_transaction['amount'] = destination_amount.get()
        transfer_transaction['created_at'] = get_datetime()
        
        all_tra = read_json('transactions.json')
        all_tra.append(transfer_transaction)
        write_json('transactions.json', all_tra)
        confirmation.destroy()
        trf.destroy()
        top.deiconify()

    def transfer_money():
        all = read_json('names.json')
        if all[index]['balance'] > destination_amount.get():
            destination_index = find_destination(destination_card.get())
            if destination_index is None:
                messagebox.showerror("No Destinatio", "Find No Destination")
            else:
                confirmation = Toplevel()
                string = f"""
From   : {all[index]['card_number']}
Name   : {all[index]['username']}

To     : {all[destination_index]['card_number']}
Name   : {all[destination_index]['username']}
Amount : {destination_amount.get()}
Do you confirm?
                """
                tk.Message(confirmation, text=string).grid(row=0, column=0)
                tk.Button(confirmation,
                    text='Confirm',
                    command=lambda: transfer_confrimation(index, destination_index, confirmation)
                ).grid(row=1, column=0, columnspan=2)
                tk.Button(confirmation,
                    text='Close',
                    command=confirmation.destroy
                ).grid(row=2, column=0, columnspan=2)

                
        else:
            messagebox.showerror("Less Money", "Not Enough Money")

    def transfer_destroy():
        trf.destroy()
        top.deiconify()
## etelaate fard ghable enteghal taiid beshe

    top.withdraw()
    trf = tk.Toplevel()
    tk.Label(trf, text='Destination').grid(row=0, column=0)
    destination_card = tk.IntVar()
    tk.Entry(trf, textvariable=destination_card).grid(row=0, column=1)
    tk.Label(trf, text='Amount').grid(row=1, column=0)
    destination_amount = tk.IntVar()
    tk.Entry(trf, textvariable=destination_amount).grid(row=1, column=1)
    tk.Button(trf, text='Transfer', command=transfer_money).grid(row=2, column=0, columnspan=2)
    tk.Button(trf, text='Close', command=transfer_destroy).grid(row=3, column=0, columnspan=2)


def get_datetime():
    frm = "%A, %H:%M:%S, %B-%d-%Y"
    return datetime.datetime.now().strftime(frm)


def read_json(address):
    with open(address) as file:
        return json.load(file)
        

def write_json(address, data):       
    with open(address, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def to_sha1(password):
    return hashlib.sha1(password.encode('utf-8')).hexdigest()


def get_card_number():
    last = read_json('names.json')
    if not last:
        return random.randint(6000000000000000, 7000000000000000)
    else:
        return last[-1]['card_number'] + random.randint(1000, 9999)


def register():
    input_user = form_user.get()
    file = read_json('names.json')
    all_users = []
    for person in file:
        all_users.append(person['username'])
    if not input_user:
        messagebox.showerror("Username Error", "Please Enter a Username")
    elif input_user not in all_users:
        if not form_pass.get():
            messagebox.showerror("Password Error", "Please Enter a Password")
        else:
            input_pass = to_sha1(form_pass.get())

            form_user.set("")
            form_pass.set("")
            file = read_json('names.json')
            data = {
                "username": input_user,
                "password": input_pass,
                "created_at": get_datetime(),
                "card_number": get_card_number(),
                "balance": 10000,
            }     
            file.append(data)
            write_json('names.json', file)
    else:
        messagebox.showerror("Username Error", "This Username is not available!")


def find_person(file, username):
    index = 0
    for person in file:
        if person['username'] == username:
            return person, index
        index += 1
    messagebox.showerror("Username Error", "Entered Invalid Username")
    return None


def login():
    global index
    username = login_user.get() 
    password = to_sha1(login_pass.get())
    file = read_json('names.json')
    person, index = find_person(file, username)
    if person is None:
        pass
    else:
        if person["password"] == password:
            top.deiconify()
            root.withdraw()
        else:
            messagebox.showerror("Password Error", "Entered Invalid Password")


deposite_transaction = {
    "type": 'deposite',
}
transfer_transaction = {
    "type": 'transfer',
}

root = tk.Tk()
root.title("Bank")

top = tk.Toplevel()
top.title("Main Menu")
top.withdraw()

note = ttk.Notebook()

register_form = tk.Frame()
login_form = tk.Frame()

note.add(register_form, text="Register")
note.add(login_form, text="Log In")

note.grid(row=0, column=0)
# register tab ################################################
tk.Label(register_form, text="Username:").grid(row=0, column=0)
tk.Label(register_form, text="Password:").grid(row=1, column=0)
form_user = tk.StringVar()
form_pass = tk.StringVar()
tk.Entry(register_form, textvariable=form_user).grid(row=0, column=1)
tk.Entry(register_form, textvariable=form_pass, show='*').grid(row=1, column=1)
tk.Button(register_form, text="Register", command=register).grid(row=2, column=0, columnspan=2, sticky=tk.W+tk.E)
###############################################################
# login tab ###################################################
tk.Label(login_form, text="Username:").grid(row=0, column=0)
tk.Label(login_form, text="Password:").grid(row=1, column=0)
login_user = tk.StringVar()
login_pass = tk.StringVar()
tk.Entry(login_form, textvariable=login_user).grid(row=0, column=1)
tk.Entry(login_form, textvariable=login_pass, show='*').grid(row=1, column=1)
tk.Button(login_form, text="Login", command=login).grid(row=2, column=0, columnspan=2, sticky=tk.W+tk.E)
###############################################################
# top level ###################################################
tk.Button(top, text="Transfer", command=transfer).grid(row=0, column=0, sticky=tk.W+tk.E)
tk.Button(top, text="Deposite", command=deposite).grid(row=0, column=1, sticky=tk.W+tk.E)
tk.Button(top, text="Balance", command=balance).grid(row=1, column=0, sticky=tk.W+tk.E)
tk.Button(top, text="Change Password", command=change).grid(row=1, column=1, sticky=tk.W+tk.E)
tk.Button(top, text="EXIT", command=root.destroy).grid(row=3, column=0, columnspan=2, sticky=tk.W+tk.E)
###############################################################
root.mainloop()