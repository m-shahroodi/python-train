# برنامه ای بنویسید که چند عدد 8 رقمی تصادفی چاپ کند و آن اعدادی که کمتر از 8 رقم هستند به تعداد کمبود آن به ابتدای رقم 0 چاپ کن

import random 
for i in range(10):
    num=random.randint(1,99999999)
    temp=8-len(str(num))
    print(temp*'0',end='')
    print(num)
    
