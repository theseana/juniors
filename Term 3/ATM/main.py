import tkinter as tk
import tkinter.ttk as ttk


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
##########################
tk.Label(register_form, text="Username:").grid(row=0, column=0)
tk.Label(register_form, text="Password:").grid(row=1, column=0)
form_user = tk.StringVar()
form_pass = tk.StringVar()
tk.Entry(register_form, textvariable=form_user).grid(row=0, column=1)
tk.Entry(register_form, textvariable=form_pass).grid(row=1, column=1)
tk.Button(register_form, text="Register").grid(row=2, column=0, columnspan=2, sticky=tk.W+tk.E)
##########################
root.mainloop()