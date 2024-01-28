# def fun1(num1,num2):
#     s=num1+num2
#     print(s)
# print("------------------")
# fun1(20,30)
# print("++++++++++++++++++")
# def printStar(num):
#     #num=int(input("Enter Number for print star : "))
#     for i in range(num):
#         print("*",end='')
# printStar(int(input("Enter Number for print star : ")))

# def mul(a,b,c):
#     f=a*b*c
#     return f
# print(mul(10,20,30))

def sumAvg(a,b,c,d):
    s=a+b+c+d
    v=s/4
    return s,v
result=sumAvg(10,20,16,7)
print(f"Sum is : {result[0]}")
print(f"Avg is : {result[1]}")