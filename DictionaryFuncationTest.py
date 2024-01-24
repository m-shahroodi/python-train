# dic1={"name":"mojtaba","family":"shahroodi","age":37,"avg":19.87}
# print(dic1)
# print(dic1.get("name"))
# print(dic1.get("color"))
# print(dic1.keys())
# print(dic1.values())
# print(dic1.items())
# dic1.setdefault("color","Red")
# print(dic1.get("color"))


text1="mojtaba ali reza mehdi mohammad sara saeed saman"
dicCountChar={}
for ch in text1:
    dicCountChar.setdefault(ch,0)
    dicCountChar[ch]+=1
print(dicCountChar)
dicNew=sorted(dicCountChar)
print(dicNew)