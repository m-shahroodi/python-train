#		برنامه ای بنویسید از کاربر نام 5 نفر را دریافت کند و کاراکترهای نام ها را زیر هم چاپ کند

def showString(str1):
        for ch in str1:
            print(ch)
        print(100*'=')
#-------------------------------------
def fillList(n):
    list1=[]
    for i in range(n):
        name=input("Enter Name :")
        list1.append(name)
    return list1
#---------------------------------------
def printName(list1):
    for name in list1:
        showString(name)
#---------------------------------------
num=int(input("Enter Number of name :"))
list1=fillList(num)
printName(list1)
