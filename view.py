from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

ws = Tk()
Frm = Frame(ws)

Frm.grid()
#  Add padding to the frame
Frm.grid(padx=50, pady=10)
# Search bar
# Add padding to the search bar
ttk.Entry(Frm).grid(row=0, column=0, columnspan=2, sticky=W+E, padx=10, pady=10)
ttk.Button(Frm, text="Search").grid(row=0, column=2, sticky=W+E)

empl = [
    ("1", "Smith", "2018-01-01", "Manager"),
    ("2", "Jones", "2018-02-01", "Supervisor"),
    ("3", "Brown", "2018-03-01", "Worker"),
    ("4", "Johnson", "2018-04-01", "Worker"),
    ("5", "Williams", "2018-05-01", "Worker"),
    ("6", "Miller", "2018-06-01", "Worker"),
    ("7", "Davis", "2018-07-01", "Worker"),
    ("8", "Garcia", "2018-08-01", "Worker"),
    ("9", "Rodriguez", "2018-09-01", "Worker"),
]
rows = empl.__len__()
cols = empl[0].__len__()


# draw table
for r in range(rows):
    for c in range(cols):
        ttk.Entry(Frm).grid(row=r+1, column=c, columnspan=1, sticky=W+E)



# draw table


ttk.Button(Frm, text="Add").grid(row=1, column=4, sticky=W+E, padx= 10)
ttk.Button(Frm, text="Edit").grid(row=3, column=4, sticky=W+E, padx= 10)
ttk.Button(Frm, text="Delete").grid(row=5, column=4, sticky=W+E, padx= 10)


ws.mainloop()