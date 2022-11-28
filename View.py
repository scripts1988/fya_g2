from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from employee_database import EmployeesDatabase
from employee import Employee
from model import *

DEFAULT_HEIGHT = 70
DEFAULT_WIDTH = 200
DEFAULT_COLS = 4

class TableCanvas:
    def __init__(self,window,employee_database):
        self.window = window
        self.database = employee_database.getDatabase()
    
    def make_table(self):
        rows = len(self.database)
        header = ["ID","Name","Date of Birth","Position"]
        for i in range(0,len(header)):
            self.label = Label(self.window,text=header[i],foreground='green',font='Arial 14 bold')
            self.label.grid(row=1, column=i, columnspan = 1)           
        for row in range(rows):
            self.add_cell(self.database[row],row+1)
    
    def add_cell(self, data,row):
        info = []
        info.append(str(data.getID()))
        info.append(data.getName())
        info.append(data.getDOB())
        info.append(data.getPosition())
        for i in range(len(info)):
            self.label = Label(self.window,text=info[i])
            self.label.grid(row=row+1, column=i, columnspan = 1)
    
    def update(self,employee_database):
        self.database = employee_database.getDatabase()
        self.make_table()
    

class Application:
    def __init__(self,mainframe,employee_database):
        self.root = mainframe
        self.database = employee_database
        self.table = TableCanvas(self.root,self.database)

        self.root.grid()
        #  Add padding to the frame
        self.root.grid(padx=50, pady=10)
        self.table.make_table()
        input_name = StringVar()
        ttk.Entry(self.root,textvariable=input_name).grid(row=0, column=0, columnspan=4, sticky=W+E, padx=10, pady=10)
        ttk.Button(self.root, text="Search",command=lambda:self.search_employee_popup(input_name.get())).grid(row=0, column=4, sticky=W+E,padx=10, pady=10)
        
        ttk.Button(self.root, text="Add",command=self.add_employee_popup).grid(row=2, column=4, sticky=W+E, padx= 10)
        ttk.Button(self.root, text="Modify",command=self.modify_employee_popup).grid(row=4, column=4, sticky=W+E, padx= 10)
        ttk.Button(self.root, text="Delete",command=lambda:self.delete_employee_popup(input_name.get())).grid(row=6, column=4, sticky=W+E, padx= 10)

        ttk.Button(self.root, text="SAVE",command=self.save).grid(row=10, column=4, sticky=W+E, padx= 10,pady=10,columnspan=2,rowspan=2)
    
    def search_employee_popup(self,name):
        employee = self.database.search(name)
        if employee == None:
            messagebox.showerror("showinfo","ERROR: Try again")
            return
        popup = Toplevel()
        popup.grid()
        popup.title("Employee Information")
        id_label = ttk.Label(popup,text="ID: " + str(employee.getID()),justify='left').grid(row = 1, column = 0, sticky=W+E,padx=10, pady=10)
        name_label = ttk.Label(popup,text="Name: " + employee.getName(),justify='left').grid(row = 2, column = 0, sticky=W+E,padx=10, pady=10)
        dob_label = ttk.Label(popup,text="Date of birth: " + employee.getDOB(),justify='left').grid(row = 3, column = 0, sticky=W+E,padx=10, pady=10)
        position_label = ttk.Label(popup,text="Position: " + employee.getPosition(),justify='left').grid(row = 4, column = 0, sticky=W+E,padx=10, pady=10)
        close_button = ttk.Button(popup,text="Close",command=lambda:popup.destroy()).grid(row=6,column=0,sticky=W+E,padx=10, pady=10)

    def add_employee_popup(self):
        input_name = StringVar()
        input_dob = StringVar()
        input_position = StringVar()
        popup = Toplevel()
        popup.grid()
        popup.title("Adding new employee")
        label = ttk.Label(popup,text="Enter new employee information",justify='center')
        label.grid(row = 0, column = 0, sticky=W+E,padx=10, pady=10, columnspan = 4)
        name_entry = ttk.Entry(popup,width=40,textvariable = input_name).grid(row = 2, column = 1, sticky = W+E,padx=10, pady=10, columnspan= 2)
        name_label = ttk.Label(popup,text="Name: ",justify='left').grid(row = 2, column = 0, sticky=W+E,padx=10, pady=10)
        
        dob_entry = ttk.Entry(popup,width=40,textvariable = input_dob).grid(row = 3, column = 1, sticky = W+E,padx=10, pady=10,columnspan= 2)
        dob_label = ttk.Label(popup,text="Date of birth: ",justify='left').grid(row = 3, column = 0, sticky=W+E,padx=10, pady=10)

        position_entry = ttk.Entry(popup,width=40,textvariable = input_position).grid(row = 4, column = 1, sticky = W+E,padx=10, pady=10,columnspan= 2)
        position_label = ttk.Label(popup,text="Position: ",justify='left').grid(row = 4, column = 0, sticky=W+E,padx=10, pady=10)

        enter_button = ttk.Button(popup,text="Enter",command=lambda:self.submit(popup,"add",input_name.get(),input_dob.get(),input_position.get())).grid(row=6,column=3,sticky=W+E,padx=10, pady=10)
        close_button = ttk.Button(popup,text="Close",command=lambda:popup.destroy()).grid(row=6,column=0,sticky=W+E,padx=10, pady=10)

    def modify_employee_popup(self):
        input_name = StringVar()
        input_dob = StringVar()
        input_position = StringVar()
        popup = Toplevel()
        popup.grid()
        popup.title("Modify employee's Information")
        label = ttk.Label(popup,text="Enter the new information",justify='center')
        label.grid(row = 0, column = 0, sticky=W+E,padx=10, pady=10, columnspan = 4)
        name_entry = ttk.Entry(popup,width=40,textvariable = input_name).grid(row = 2, column = 1, sticky = W+E,padx=10, pady=10, columnspan= 2)
        name_label = ttk.Label(popup,text="Name: ",justify='left').grid(row = 2, column = 0, sticky=W+E,padx=10, pady=10)
        
        dob_entry = ttk.Entry(popup,width=40,textvariable = input_dob).grid(row = 3, column = 1, sticky = W+E,padx=10, pady=10,columnspan= 2)
        dob_label = ttk.Label(popup,text="Date of birth: ",justify='left').grid(row = 3, column = 0, sticky=W+E,padx=10, pady=10)

        position_entry = ttk.Entry(popup,width=40,textvariable = input_position).grid(row = 4, column = 1, sticky = W+E,padx=10, pady=10,columnspan= 2)
        position_label = ttk.Label(popup,text="Position: ",justify='left').grid(row = 4, column = 0, sticky=W+E,padx=10, pady=10)

        enter_button = ttk.Button(popup,text="Enter",command=lambda:self.submit(popup,"modify",input_name.get(),input_dob.get(),input_position.get())).grid(row=6,column=3,sticky=W+E,padx=10, pady=10)
        close_button = ttk.Button(popup,text="Close",command=lambda:popup.destroy()).grid(row=6,column=0,sticky=W+E,padx=10, pady=10)

    def delete_employee_popup(self,name):
        employee = self.database.search(name)
        if employee == None:
            messagebox.showerror("showinfo","ERROR: Try again")
            return
        popup = Toplevel()
        popup.grid()
        popup.title("Employee Information")
        id_label = ttk.Label(popup,text="ID: " + str(employee.getID()),justify='left').grid(row = 1, column = 0, sticky=W+E,padx=10, pady=10)
        name_label = ttk.Label(popup,text="Name: " + employee.getName(),justify='left').grid(row = 2, column = 0, sticky=W+E,padx=10, pady=10)
        dob_label = ttk.Label(popup,text="Date of birth: " + employee.getDOB(),justify='left').grid(row = 3, column = 0, sticky=W+E,padx=10, pady=10)
        position_label = ttk.Label(popup,text="Position: " + employee.getPosition(),justify='left').grid(row = 4, column = 0, sticky=W+E,padx=10, pady=10)
        cancel_button = ttk.Button(popup,text="Cancel",command=lambda:popup.destroy()).grid(row=6,column=0,sticky=W+E,padx=10, pady=10)
        delete_button = ttk.Button(popup,text="Delete",command=lambda:self.submit(popup,"delete",name)).grid(row=6,column=4,sticky=W+E,padx=10, pady=10)

    def submit(self,popup,command,name,dob="",position=""):
        worker = Employee()
        worker.setName(name)
        worker.setDOB(dob)
        worker.setPosition(position)
        if command == "add" and name != "":
            ret_val = self.database.add(worker.getName(),worker.getDOB(),worker.getPosition())
        elif command == "modify" and name != "":
            ret_val = self.database.modify(worker.getName(),worker.getDOB(),worker.getPosition())
        elif command == "search":
            ret_val = self.database.search(name)
        else:
            ret_val = self.database.delete(name)
        if ret_val:
            self.table.make_table()
            write_file(self.database,'temp.csv')
            popup.destroy()
            messagebox.showinfo("showinfo","SUCCESS")
        else:
            messagebox.showerror("showinfo","ERROR: Try again")
    
    def save(self):
        write_file(self.database)
        self.table.update(self.database)

