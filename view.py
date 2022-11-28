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

width = 700
height = 450

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("{width}x{height}".format(width= width, height= height))



class TableCanvas:
    def __init__(self, data=empl):
        self.rows = data.__len__()
        self.cols = data[0].__len__()
        self.empl = data
    
        for row in range(self.rows):
            for col in range(self.cols):
                self.add_cell(row, col)

    def add_cell(self, row, col):  
        text_var = tkinter.StringVar(value=empl[row][col]) 
        self.label = customtkinter.CTkLabel(master=app,textvariable=text_var,width=120,height=30,fg_color=("white", "gray75"),text_color=("black","black"),)
        self.label.grid(row=row+1, column=col, columnspan = 1)


class Input:
    def __init__(self,row, column, placeholder, window=app):
        self.entry = customtkinter.CTkEntry(master=window,placeholder_text=placeholder,height=32,border_width=2,corner_radius=4,width=200)
        self.entry.grid(row = row, column = column, padx = (50, 0), pady = 20, columnspan = 3)
        
    def get_text(self):
        return self.entry.get()

        
class Button:
    def __init__(self, row, column, label, columnspan = None, func = None, pady = 20, window = app):
        self.button = customtkinter.CTkButton(master=window, text=label, command=func, height = 28, width=80)
        self.button.grid(row= row, column= column, padx = 10, pady = pady, columnspan = 1)

def add():
    print("add button pressed") 

    top= Toplevel(app)
    top.geometry("600x350")
    top.title("Child Window")

    # Input
    name_entry = Input(0,0,"Name", window=top)
    dob_entry = Input(0,3,"DoB", window=top)
    position_entry = Input(1,0,"Position", window=top)

    def update():
        name = name_entry.get_text()
        dob = dob_entry.get_text()
        pos = position_entry.get_text()
        empl.append((len(empl), name, pos, dob)) # Do some thing here

        # Update table in the main window
        TableCanvas().add_cell(empl.__len__()-1,empl[0].__len__()-1)
        
    # Two button
    Button(4,2,"OK",delete,func=update,pady=20, window=top)
    Button(4,4,"Cancel",delete,func=top.destroy, pady=20, window=top)



def edit():
    print("edit button pressed")
    top= Toplevel(app)
    top.geometry("900x350")
    top.title("Child Window")

    # Input
    name_entry = Input(0,0,"Name", window=top)
    dob_entry = Input(0,3,"DoB", window=top)
    position_entry = Input(0,6,"Position", window=top)

    # New entry
    name_entry_new = Input(1,0,"New Name", window=top)
    dob_entry_new = Input(1,3,"New DoB", window=top)
    position_entry_new = Input(1,6,"New Position", window=top)

    def update():
        name = name_entry.get_text()
        dob = dob_entry.get_text()
        pos = position_entry.get_text()

        new_name = name_entry_new.get_text()
        new_dob = dob_entry_new.get_text()
        new_pos = position_entry_new.get_text()

        map = {name:new_name,
            dob:new_dob,
            pos:new_pos}
        # Do some thing here - edit function

    # Two button
    Button(4,3,"OK",delete,func=update,pady=20, window=top)
    Button(4,6,"Cancel",delete,func=top.destroy, pady=20, window=top)

def delete():
    print("delete button pressed")
    top= Toplevel(app)
    top.geometry("600x350")
    top.title("Child Window")
    name_entry = Input(0,0,"Name", window=top)
    dob_entry = Input(0,3,"DoB", window=top)
    position_entry = Input(1,0,"Position", window=top)
    
    def update():
        name = name_entry.get_text()
        dob = dob_entry.get_text()
        pos = position_entry.get_text()
        # Do something here - delete function
        
    Button(4,2,"OK",delete,func=update,pady=20, window=top)
    Button(4,4,"Cancel",delete,func=top.destroy, pady=20, window=top)
        
if __name__ == "__main__":
    Input(0,0,"Search for employees...")
    Button(0,3, "Search")
    TableCanvas()
    Button(1, 5, "Add employees", add, pady=0, func=add)
    Button(3, 5, "Delete employees", delete, pady=0, func=delete)
    Button(5, 5, "Edit employees", edit, pady=0, func=edit)
    app.mainloop()