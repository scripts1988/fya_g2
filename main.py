from employee_database import EmployeesDatabase
from model import *

# # testing space
EmployeeList = read_file()

#employee_list.print()

# ret = EmployeeList.add("Debbie","20/20/97","Admin")
# ret = EmployeeList.add("Fiona","01/02/97","CTO")
# ret = EmployeeList.add("Emma","51/02/98","Marketing")
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

# ret = EmployeeList.add("Anna","22/06/00","HR")
# print(ret)
# EmployeeList.print()

# ret = EmployeeList.add("Rosie")
# print(ret)
# EmployeeList.print()

EmployeeList.modify("Rosie", "20/09/02", "Sales Assisant")
#EmployeeList.print()

write_file(EmployeeList)
EmployeeList = read_file()
EmployeeList.print()