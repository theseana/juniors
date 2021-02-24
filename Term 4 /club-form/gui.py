import tkinter as tk
import random
from tkinter import filedialog

from tkcalendar import DateEntry

from database.connection import Connection
from database.models import Member


class GUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        frame_r = tk.LabelFrame(self, text="Register")
        frame_r.grid(row=0, column=0)

        tk.Label(frame_r, text="First Name").grid(row=0, column=0)
        self.name = tk.StringVar()
        tk.Entry(frame_r, textvariable=self.name).grid(row=0, column=1)

        tk.Label(frame_r, text="Last Name").grid(row=1, column=0)
        self.last = tk.StringVar()
        tk.Entry(frame_r, textvariable=self.last).grid(row=1, column=1)

        tk.Label(frame_r, text="Birth").grid(row=2, column=0)
        self.birth = tk.StringVar()
        DateEntry(frame_r, textvariable=self.birth, date_pattern="y-mm-dd",
            background='darkblue', foreground='white').grid(row=2, column=1)

        tk.Label(frame_r, text="Image").grid(row=3, column=0)
        self.filename = tk.StringVar()
        tk.Button(frame_r, text="Browse", command=self.browse_func).grid(row=3, column=1)

        tk.Button(frame_r, text="Create", command=self.create).grid(row=5, column=0)
    
        frame_d = tk.LabelFrame(self, text="Delete")
        frame_d.grid(row=1, column=0)

        self.id_del = tk.IntVar()
        tk.Entry(frame_d, textvariable=self.id_del).grid(row=0, column=0)
        tk.Button(frame_d, text="Delete", command=self.delete).grid(row=0, column=1)
        
        frame_u = tk.LabelFrame(self, text="Update")
        frame_u.grid(row=0, column=1)
        
        tk.Label(frame_u, text="ID").grid(row=0, column=0)
        self.id_u = tk.IntVar()
        tk.Entry(frame_u, textvariable=self.id_u).grid(row=0, column=1)

        tk.Label(frame_u, text="First Name").grid(row=1, column=0)
        self.name_u = tk.StringVar()
        tk.Entry(frame_u, textvariable=self.name_u).grid(row=1, column=1)

        tk.Label(frame_u, text="Last Name").grid(row=2, column=0)
        self.last_u = tk.StringVar()
        tk.Entry(frame_u, textvariable=self.last_u).grid(row=2, column=1)

        tk.Label(frame_u, text="Birth").grid(row=3, column=0)
        self.birth_u = tk.StringVar()
        DateEntry(frame_u, textvariable=self.birth_u, date_pattern="y-mm-dd",
            background='darkblue', foreground='white').grid(row=3, column=1)

        tk.Label(frame_u, text="Image").grid(row=4, column=0)
        self.filename_u = tk.StringVar()
        tk.Button(frame_u, text="Browse", command=self.browse_func).grid(row=4, column=1)

        tk.Button(frame_u, text="Update", command=self.up).grid(row=5, column=0)
    
        frame_s = tk.LabelFrame(self, text="Search")
        frame_s.grid(row=1, column=1)

        self.id_s = tk.IntVar()
        tk.Entry(frame_s, textvariable=self.id_s).grid(row=0, column=0)
        tk.Button(frame_s, text="Search ID", command=self.id_s).grid(row=0, column=1)

    def up(self):   
        session = Connection().create_session()
        person = session.query(Member).filter(Member.member_id == self.id_u.get()) 
        person.update({
            'first_name': self.name_u.get(),
            'last_name': self.last_u.get(),
            'image': self.filename_u.get(),
            'birth_date': self.birth_u.get()
        })
        session.commit()

    def delete(self):   
        session = Connection().create_session()
        person = session.query(Member).filter(Member.member_id == self.id_del.get()) 
        person.delete()
        session.commit()

    def browse_func(self):
        self.filename.set(filedialog.askopenfilename())

    def create(self):
        name = self.name.get()
        last = self.last.get()
        image = self.filename.get()
        birth = self.birth.get()
        id_ = self.get_id()

        session = Connection().create_session()
        member = Member(name, last, image, birth, id_)

        session.add(member)
        session.commit()
    
    def get_id(self):
        return random.randint(1, 10000)

    def main(self):
        self.mainloop()
