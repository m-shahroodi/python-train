# 	برنامه مربوط به مدرسه که دارای کلاس دانش آموزان ، اساتید و دروس باشد 
class Student:
    def __init__(self,name,family,address,age):
        self.name=name
        self.family=family
        self.address=address
        self.age=age
    def __str__(self):
        return f"Name :{self.name}/t/tFamily :{self.family}/t/tAddress :{self.address}/t/tAge :{str(self.age)}"
#-----------------------------------------------------------------------------------------------------------
class Teacher:
    def __init__(self,name,family,address,tel):
        self.name=name
        self.family=family
        self.address=address
        self.tel=tel
    def __str__(self):
        return f"Name :{self.name}/t/tFamily :{self.family}/t/tAddress :{self.address}/t/tTel :{self.tel}"
#-----------------------------------------------------------------------------------------------------------
class Dars:
    def __init__(self,darsName,numberVahed):
        self.darsName=darsName
        self.numberVahed=numberVahed
    def __str__(self):
        return f"Dars :{self.darsName}/t/tVahed :{str(self.numberVahed)}"    

#-----------------------------------------------------------------------------------------------------------
class School:
    def __init__(self,schoolName):
        self.schoolName=schoolName
        self.teacherList=[]
        self.studentList=[]
        self.darsList=[]
    def addTeacher(self,t):
        self.teacherList.append(t)
        
    def addStudent(self,s):
        self.studentList.append(s) 
        
    def addDars(self,d):
        self.darsList.append(d) 
           
    def showListOfStudent(self):
        for s in self.studentList:
            print(s)
#-----------------------------------------------------------------------------------------------------------
s=School("SHAHROODI")
ss2=School("SHAHROODI")

t1=Teacher("Mojtaba","Shahroodi","Tehran","09121111111")
d1=Dars("Riazi",3)
s1=Student("Ali","Rezaei","Tehran",19.5)
s2=Student("Reza","Ahmadi","Tehran",18.5)

s.addStudent(s1)
ss2.addStudent(s2)

#s.showListOfStudent()
s.showListOfStudent()
print("go to next Instaace")
ss2.showListOfStudent()