while True :
   d=int(input("Please Enter day :"))
   if 0<d and d<=31:
      break
   else:
      print("Please Enter True day")
while True:
   m=int(input("Please Enter Month :")) 
   if m>0 and m<=12:
      break
   else:
      print("Please Enter True month")
if 1<=m and m<=6: 
   day=(m-1)*31+d
   print(day)
elif 7<=m and m<=12:
     day=(m-1)*30+6+d
     print(day)

