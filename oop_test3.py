class Car:
    count=0
    def __init__(self,color,brand,weight,capacity,maxSpeed):
        self.color=color
        self.brand=brand
        self.weight=weight
        self.capacity=capacity
        self.maxSpeed=maxSpeed
        Car.count+=1
    
    def __str__(self):
        return f"Brand : {self.brand}\tcolor :{self.color}\tMax Speed :{self.maxSpeed}\t"
    
    def startEngine(self):
        print("Start Car")
    
    def stopEngine(self):
        print("Stop Car")
    
    def accelerate(self):
        print("Accelerate Car")

print(Car.count)
car1=Car("blue","benz",3400,5,260)
car2=Car("black","mvm",1790,4,180)
car3=Car("red","prid",1900,6,360)
print(Car.count)
