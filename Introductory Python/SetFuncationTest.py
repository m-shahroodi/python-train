# set1={12,45,78,345,897}
# set2={15,68,12,100,78}
# temp=set1.difference(set2)
# print(temp)
# temp2=set2.difference(set1)
# print(temp2)

set1={12,45,78,345,897}
set2={15,68,12,100,78}
set3={15,12}
set4=set1.union(set2)
set5=set1.intersection(set2)
print(set4)
print(set5)
print(set1.issubset(set2))
print(set3.issubset(set2))