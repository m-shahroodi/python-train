# برنامه بنویسید که لیست از اعداد صحیح مثبت از کاربر بگیرد و آن را چاپ کند و در ادامه یک عدد برای جستجو در لیست اعداد بگیرد و وجود یا عدم وجود عدد را نشان دهد

def readNumber():
    list1=[]
    num=int(input('Enter Number : '))
    while num>=0 :
        list1.append(num)
        num=int(input('Enter Number : '))
    return list1
#----------------------------------------------
def printNumbers(list1):
    for item in list1:
        print(item,end='\t')
    print()
#----------------------------------------------
def search(list1,x):
    count=0
    for item in list1:
        if item==x:
            count+=1
    if count>0:
        print(f"{count} Number Found ...")
    else:
        print('Number Not Found ...')
#----------------------------------------------
numbers=readNumber()
printNumbers(numbers)
num=int(input("Enter Number For Search :"))
search(numbers,num)
