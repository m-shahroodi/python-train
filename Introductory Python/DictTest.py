# dict1={'red':24,'blue':80,'yellow':200,'green':60,'blue':250}
# print(dict1)
# print(dict1['yellow'])
# dict1['yellow']=1000
# print(dict1)
# dict1['black']=500
# print(dict1)

# student={'studentId':1,
#          'name':'Reza',
#          'family':'Ahmadi',
#          'age':23,
#          'avg':15.67,
#          'courses':{'fizik':13.45,'riyazi':17.6,'farsi':19,'arabi':11}
#          }
# print(student['courses'])

# dic1={'red':24,'blue':80,'yellow':200,'green':60}
# for i in dic1:
#     print(i,end=' *** ') 
# print()
# for value in dic1.values():
#     print(value,end=' *** ') 
# print()
# for key in dic1.keys():
#     print(key,end=' *** ') 
# print()
# for item in dic1.items():
#     print(item,end=' *** ') 
# print()

dic1={'red':24,'blue':80,'yellow':200,'green':60}
print(dic1['yellow'])
print(dic1.get('yellow'))