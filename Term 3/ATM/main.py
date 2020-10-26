import tkinter as tk
import tkinter.ttk as ttk
import hashlib


def to_sha1(password):
    return hashlib.sha1(password.encode('utf-8')).hexdigest()


def register():
    input_user = form_user.get()
    input_pass = to_sha1(form_pass.get())
    form_user.set("")
    form_pass.set("")
    with open('users.txt', 'a') as file:
        file.write(f"user:{input_user} pass:{input_pass}\n")


def login():
    passs        
root = tk.Tk()
root.title("Bank")

# top = tk.Toplevel()
# top.title("Form")

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
root.mainloop()