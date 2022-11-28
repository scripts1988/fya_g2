# enclose an employee's information
class Employee:

    # initialize
    def __init__(self, name = "", date_of_birth = "", position = ""):
        self.ID = 0
        self.name = name
        self.date_of_birth = date_of_birth
        self.position = position

    def getID(self):
        return self.ID
    
    def getName(self):
        return self.name
    
    def getDOB(self):
        return self.date_of_birth
    
    def getPosition(self):
        return self.position
    
    def setID(self, id):
        self.ID = id

    def setName(self,name):
        self.name = name
    
    def setDOB(self,dob):
        self.date_of_birth = dob
    
    def setPosition(self,role):
        self.position = role
    
    # string format to print
    def __str__(self):
        return f'{self.ID: <2}: {self.name: <15}  {self.date_of_birth: ^12} {self.position: ^15}'
 