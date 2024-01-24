# list1=[22,34,565,767,556,553]
# list2=["Mojtaba","Ali","Reza","Sahar","Sara"]
# list3=[22.3,455.55,767.55]
# list4=[True,False,True,True]
# list5=[100,"Mojtaba",5525,888.5,True,"Reza"]

# print(list2)
# print(type(list2))
# for name in list2:
#     print(name,end=' ')
# print()
# for i in range(len(list2)):
#     print(list2[i],end=' ')

# list2=["Mojtaba","Ali","Reza","Sahar","Sara"]
# numbers=[22,34,565,767,556,553]
# numbers.extend([111,222,333,444])
# print(numbers)
# numbers.extend(list2)
# print(numbers)


# numbers=[22,34,22,565,22,767,22,556,553]
# numbers.remove(22)
# print(numbers)


name="mehdi"
temp=list(name)
temp[0]='M'
temp=''.join(temp)
print(temp)