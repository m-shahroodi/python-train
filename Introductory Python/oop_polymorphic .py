# def sum(a,b,c=0):
#     return a+b+c
# print(sum(10,20,30))
# print(sum(10,20))

class Person:
    def __init__(self,name,family,age):
        self.name = name
        self.family = family
        self.age = age
    def __str__(self):
        return self.name+" "+self.family+" "+self.age
    def show(self):
        print("Person...")
#--------------------------------------------------------------
class Student(Person):
    def __init__(self,studentId,name,family,age):
        Person.__init__(self,name,family,age)
        self.studentId = studentId
    def show(self):
        print("Student ...")
#--------------------------------------------------------------
class Teacher(Person):
    def __init__(self,teachertId,name,family,age):
        Person.__init__(self,name,family,age)
        self.teachertId = teachertId
#--------------------------------------------------------------
s1=Student(1000,'Ali','Ahmadi',19)
t1=Teacher(100,'Reza','Akbari',20)
s1.show()
t1.show()