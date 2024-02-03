#	برنامه ای بنویسید تا وقتی عدد منفی وارد نشده است تمام اعداد را از ورودی دریافت و حاصل جمع آنها را محاسبه نماید
sum = 0
num = int(input("Enter Number :"))
while num >= 0 :
    sum+=num 
    num = int(input("Enter Number :"))
print("Result is :",sum) 
