# def showPersonInfo(name,family,address,mobileNumber,age):
#     print(f"FullName : {name} {family}")
#     print(f"Address : {address}")
#     print(f"MobileNumber : {mobileNumber}")
#     print(f"Age : {age}")

# showPersonInfo(name='Mojtaba',family='Shahroodi',age=37,mobileNumber='09124309728',address='Tehran')

# def sum(a,b,c=0,d=0):
#     return a+b+c+d
# print(sum(10,20,30,40))
# print(sum(10,20,30))
# print(sum(10,20))

# def showList(list1):
#     for item in list1:
#         print(item,end='\t')
#     print()

# showList([123,43,543,654,85,475])
# showList(["Mojtaba","Reza","Ali","Sara","Sahar","Negin"])

# import random
# def getRandomList(n):
#     list1=[]
#     for i in range(n):
#         list1.append(random.randint(1,100))
#     return list1
# tempList=getRandomList(10)
# print(tempList)

def fun1(*args):
    for item in args:
        print(item,end='\t')
fun1(12,"ali",True,"reza",2525,665,5445)
    