num=int(input("Enter number : "))
c=0 
while num>0 :
    num//=10
    c+=1
print(c)