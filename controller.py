

# enclose an employee's information
class EmployeeData:

    # initialize
    def __init__(self, name = "", date_of_birth = "", position = ""):
        self.ID = 0
        self.name = name
        self.date_of_birth = date_of_birth
        self.position = position
    
    # string format to print
    def __str__(self):
        return f'{self.ID: <2}: {self.name: <15}  {self.date_of_birth: ^12} {self.position: >15}'

# data structure to manage all employees
class Employees:

    # initialize
    def __init__(self):
        self.employee_list = []
        self.max_size = 20

    # print function
    def print(self):
        for worker in self.employee_list:
            print(worker)

    # search by name
    # return: employee's module if found, otherwise: None (NULL)
    def search(self,name):
        for employee in self.employee_list:
            if (employee.name == name):
                return employee
        return None

    # add by name, DOB, Position
    # return true if successfully added.
    # Return false: the employee with the same name and DOB exists or the list reaches the limit allowed (max_size)
    def add(self,name, dob = "", position = ""):
        # The employee is already in the list
        employee = self.search(name)

        # if the new employee is existed and the position is the same OR over the limit
        if (employee != None) and (employee.date_of_birth == dob) or (len(self.employee_list) > self.max_size):
            return False

        new_employee = EmployeeData(name,dob,position)
        # Id is assigned based on adding order (1st employee: 1, 20th employee: 20)
        new_employee.ID = len(self.employee_list) + 1
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
            employee.date_of_birth = date_of_birth
        if position != "":
            employee.position = position
        return True


# # testing space

# EmployeeList = Employees()
# ret = EmployeeList.add("Sarah","20/20/96","COO")
# ret = EmployeeList.add("Hannah","51/02/96","CEO")
# ret = EmployeeList.add("Hannah","51/02/98","Marketing")
# print(ret)
# EmployeeList.print()
# ret = EmployeeList.modify("Sarah","20/02/96")
# print(ret)
# EmployeeList.print()

# ret = EmployeeList.delete("Rosie")
# print(ret)
# EmployeeList.print()

# ret = EmployeeList.add("Rosie","20/05/02","Sales")
# print(ret)
# EmployeeList.print()

# ret = EmployeeList.delete("Rosie")
# print(ret)
# EmployeeList.print()

# ret = EmployeeList.add("Dennis","20/05/00","HR")
# print(ret)
# EmployeeList.print()

# ret = EmployeeList.add("Rosie")
# print(ret)
# EmployeeList.print()

# EmployeeList.modify("Rosie", "20/05/02", "Sales")
# print(ret)
# EmployeeList.print()