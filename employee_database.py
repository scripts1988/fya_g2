
from employee import Employee
# data structure to manage all employees
class EmployeesDatabase:
    # initialize
    def __init__(self):
        self.employee_list = []
        self.max_size = 20

    def getDatabase(self):
        return self.employee_list
    
    # print function
    def print(self):
        if (len(self.employee_list) == 0):
            print("No employee data is available")
            return
        for worker in self.employee_list:
            print(worker)

    # Id is assigned based on adding order (1st employee: 1, 20th employee: 20)
    def generateID(self):
        if (len(self.employee_list) == 0):
            return 1
        return (self.employee_list[-1].getID() + 1)
        

    # search by name
    # return: employee's module if found, otherwise: None (NULL)
    def search(self,name):
        for employee in self.employee_list:
            if (employee.name == name):
                return employee
        return None

    # add by name, DOB, Position
    # return true if successfully added.
    # Return false: the employee with the same name exists or the list reaches the limit allowed (max_size)
    def add(self,name, dob = "", position = "", id = 0):
        # The employee is already in the list
        employee = self.search(name)

        # if the new employee is existed OR the list is at the limit
        if (employee != None) or (len(self.employee_list) > self.max_size):
            return False

        new_employee = Employee(name,dob,position)
        if (id == 0):
            new_employee.setID(self.generateID())
        else:
            new_employee.setID(id)
        
        self.employee_list.append(new_employee)
        return True

    # delete employee by name
    # return false if the employee's name is not in the list
    # return true if the employee is found and deleted
    def delete(self,name):
        employee = self.search(name)
        if employee == None:
            return False

        self.employee_list.remove(employee)
        return True
    
    # change DOB or position
    # cannot change name!
    # modify by searching for name
    def modify(self,name,date_of_birth = "",position = ""):
        employee = self.search(name)
        if employee == None:
            return False
        if date_of_birth != "":
            employee.setDOB(date_of_birth)
        if position != "":
            employee.setPosition(position)
        return True
