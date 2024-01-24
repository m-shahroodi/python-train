class Car:
    def __init__(self,color,brand,weight,capacity,maxSpeed):
        self.color=color
        self.brand=brand
        self.weight=weight
        self.capacity=capacity
        self.maxSpeed=maxSpeed
    
    def startEngine(self):
        print("Start Car")
    
    def stopEngine(self):
        print("Stop Car")
    
    def accelerate(self):
        print("Accelerate Car")

car1=Car("blue","benz",3400,5,260)
car2=Car("black","mvm",1790,4,180)
car3=Car("red","prid",1900,6,360)
print(car1.color,car1.brand,car1.weight,car1.capacity,car1.maxSpeed)
print(car2.color,car2.brand,car2.weight,car2.capacity,car2.maxSpeed)
print(car3.color,car3.brand,car3.weight,car3.capacity,car3.maxSpeed)
car1.startEngine()
car2.stopEngine()
car3.accelerate()