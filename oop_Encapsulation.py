class Person:
    def __init__(self,name,family,age):
        self.__name = name
        self.__family = family
        self.age = age
    def __str__(self):
        return self.__name+"\t"+self.__family+"\t"+str(self.age)
    def __fun1():
        print("Hello")
#-----------------------------------------------------------------
p1=Person("Mojtaba","Shahroodi",37)
print(p1)
p1.__name="Ali"
p1.age=40
print(p1)
        