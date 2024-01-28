class Person:
    def __init__(self,name,family,phone,address):
        self.name = name
        self.family = family
        self.phone = phone
        self.address = address
    
    def showInfo(self):
        print(self)
#------------------------------------------------------------------------------------------------------------------
class Student(Person):
    def __init__(self,shNumber,name,family,phone,address):
        super().__init__(name,family,phone,address)
        self.shNumber = shNumber
        
    def __str__(self) :
        return str(self.shNumber) + " " + self.name + " " + self.family + " " + self.phone + " " + self.address
#------------------------------------------------------------------------------------------------------------------
class Teacher(Person):
    def __init__(self,teacherCode,name,family,phone,address):
        super().__init__(name,family,phone,address)
        self.teacherCode = teacherCode
        
    def __str__(self) :
        return str(self.teacherCode) + " " + self.name + " " + self.family + " " + self.phone + " " + self.address
#------------------------------------------------------------------------------------------------------------------
class Employee(Person):
    def __init__(self,employeeId,name,family,phone,address):
        super().__init__(name,family,phone,address)
        self.employeeId = employeeId
        
    def __str__(self) :
        return str(self.employeeId) + " " + self.name + " " + self.family + " " + self.phone + " " + self.address
#------------------------------------------------------------------------------------------------------------------
s1=Student(1200,'Ali','Rezaei','0912000000','Tehran')
t1=Teacher(11350,'Mojtaba','Shahroodi','0912111111','Tehran')
emp1=Employee(100,'Reza','Akbari','0912010101','Arak')
t1.showInfo()
s1.showInfo()
emp1.showInfo()