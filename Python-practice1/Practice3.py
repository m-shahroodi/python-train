#	برنامه بنویسید که به دلخواه کاربر تعداد سطر و ستون از ورودی بگیرد و ستاره چاپ کند 

# row = int(input("Enter row :"))
# col = int(input("Enter col :"))
# for i in range(row):
#     for j in range(col):
#         print("*",end="")
#     print()

# row = int(input("Enter row :"))
# col = int(input("Enter col :"))
# for i in range(row):
#     print(col*"*")

# row = int(input("Enter row :"))
# for i in range(row):
#     print(i*"*")
    
    
# for i in range(1,11,1):
#     print(i*"*".center(5))
# for j in range(11,0,-1):
#     print(j*"*".center(5))

# برنامه چاپ ستاره ها که به شکل لوزی را تشکیل می دهند

for i in range(0,22,1):
    if i%2 == 0 : continue 
    print(int(((22-i)/2))*' ', end='')
    print(i*"*")
    
for j in range(22,0,-1):
    if j%2 == 0 : continue 
    print(int(((22-j)/2))*' ',end='')
    print(j*"*")
    