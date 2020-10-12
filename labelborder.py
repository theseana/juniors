from tkinter import *

app = Tk()

labelExample1 = Label(app,
                     borderwidth=1,
                     width=40,
                     relief="raised",
                     text="raised & borderwidth=1")
labelExample2 = Label(app,
                     borderwidth=2,
                     width=40,
                     relief="ridge",
                     text="ridge & borderwidth=2")
labelExample3 = Label(app,
                     borderwidth=3,
                     width=40,
                     relief="sunken",
                     text="sunken & borderwidth=3")
labelExample4 = Label(app,
                     borderwidth=4,
                     width=40,
                     relief="flat",
                     text="flat & borderwidth=4")
labelExample5 = Label(app,
                     borderwidth=5,
                     width=40,
                     relief="groove",
                     text="groove & borderwidth=5")
labelExample6 = Label(app,
                     borderwidth=6,
                     width=40,
                     relief="ridge",
                     text="solid & borderwidth=6")

labelExample1.grid(column=0, row=0, padx=10, pady=10)
labelExample2.grid(column=0, row=1, padx=10, pady=10)
labelExample3.grid(column=0, row=2, padx=10, pady=10)
labelExample4.grid(column=0, row=3, padx=10, pady=10)
labelExample5.grid(column=0, row=4, padx=10, pady=10)
labelExample6.grid(column=0, row=5, padx=10, pady=10)
app.mainloop()
