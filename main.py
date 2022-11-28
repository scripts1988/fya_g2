from employee_database import EmployeesDatabase
from model import *
from View import *



def main():
    root = Tk()
    App = Frame(root)
    # Search bar
    # Add padding to the search bar
    employee_database = read_file()

    Application(App,employee_database)
    root.mainloop()

if __name__ == '__main__':
    main()