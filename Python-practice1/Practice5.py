# برنامه ای بنویسید که اعضای یک لیست عددی یک رقمی از ورودی دریافت کند و به ازای هر کدام از اعضا به تعداد همان عدد ستاره چاپ کند و اگر صفر بود چیزی برای آن عضو چاپ نکند
list1=[]
num=int(input("Enter Number :"))
while(0<=num and num<=9):
    list1.append(num)
    num=int(input("Enter Number :"))
list2=[]
for i in list1:
    if i != 0:
        list2.append(i*"*")
print(list2)