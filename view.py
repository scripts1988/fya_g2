import customtkinter
import tkinter
from tkinter import *
from tkinter import ttk

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
 
empl = [
    ("Index", "Name", "DoB", "Role"),
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

width = 700
height = 450

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("{width}x{height}".format(width= width, height= height))

class TableCanvas:
    def __init__(self):
        self.rows = rows
        self.cols = cols
        self.empl = empl
    
        for row in range(self.rows):
            for col in range(self.cols):
                self.add_cell(row, col)

    def add_cell(self, row, col):  
        text_var = tkinter.StringVar(value=empl[row][col]) 
        self.label = customtkinter.CTkLabel(master=app,textvariable=text_var,width=120,height=30,fg_color=("white", "gray75"),text_color=("black","black"),)
        self.label.grid(row=row+1, column=col, columnspan = 1)
def add():
    print("add button pressed")

def edit():
    print("edit button pressed")

def delete():
    print("delete button pressed")

class Input:
    def __init__(self,row, column, placeholder):
        self.entry = customtkinter.CTkEntry(master=app,placeholder_text=placeholder,height=32,border_width=2,corner_radius=4,width=200)
        self.entry.grid(row = row, column = column, padx = (50, 0), pady = 20, columnspan = 3)
        
class Button:
    def __init__(self, row, column, label, columnspan = None, func = None, pady = 20):
        self.button = customtkinter.CTkButton(master=app, text=label, command=func, height = 28, width=80)
        self.button.grid(row= row, column= column, padx = 10, pady = pady, columnspan = 1)

Input(0,0,"Search for employees...")
Button(0,3, "Search")
TableCanvas()
Button(1, 5, "Add employees",add, pady=0)
Button(3, 5, "Delete employees",delete, pady=0)
Button(5, 5, "Edit employees",edit, pady=0)

app.mainloop()