# def fun(x):
#     return x*100
# print(fun(20))

# fun=lambda x: x*100
# print(fun(20))

# getFullName=lambda name,family: name+" "+family
# print(getFullName('Mojtaba','Shahroodi'))

# print((lambda name,family: f"{name} {family}")('Mojtaba','Shahroodi'))

# def sum(num1,num2):
#     return num1+num2
# def sub(num1,num2):
#     return num1-num2
# def mul(num1,num2):
#     return num1*num2
# def div(num1,num2):
#     return num1/num2
# def fun(x,y,funcName):
#     print(funcName(x,y))
# fun(100,40,sum)
# fun(100,40,sub)
# fun(100,40,mul)
# fun(100,40,div)

# fun = lambda x,y,funcName:funcName(x,y)
# print(fun(100,40,lambda num1,num2:num1+num2))
# print(fun(100,40,lambda num1,num2:num1-num2))
# print(fun(100,40,lambda num1,num2:num1*num2))
# print(fun(100,40,lambda num1,num2:num1/num2))

# names=['mehdi13','mehdi5','mehdi2','mehdi49','mehdi25','mehdi31']
# print(sorted(names))
# print(sorted(names,key=lambda x:int(x[5:])))

# dicList=[
#     {"name":'mehdi',"age":43},
#     {"name":'ali',"age":82},
#     {"name":'mehdi',"age":21},
#     {"name":'ahmad',"age":39}
# ]
# print(sorted(dicList,key=lambda dic:dic["name"]))