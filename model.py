from employee_database import EmployeesDatabase
from employee import Employee

# absolute file path
#file_path = '/Users/148865/Documents/fya_g2/data.csv'

# relative file path
file_path = 'data.csv'

# read data from csv file
def read_file(file_directory = file_path):
    employee_list = EmployeesDatabase()
    try:
        with open(file_directory) as file:
            for line in file.readlines():
                info = line.strip()
                data = info.split(',')
                # 0 : ID
                # 1 : Name
                # 2 : DOB
                # 3 : Position
                employee_list.add(data[1],data[2],data[3],int(data[0]))
    except:
        print('Error finding file... EXIT')
    return employee_list

# write to csv file from the employee list
def write_file(employee_database, file_directory = file_path):
    try:
        with open(file_directory,"w") as file:
            for employee in employee_database.employee_list:
                # csv file format: ID,name,DOB,position
                data_set = [str(employee.getID()),employee.getName(),employee.getDOB(),employee.getPosition()]
                info = ','.join(data_set)
                file.write(info)
                file.write('\n')
    except:
        print('Error finding file... EXIT')