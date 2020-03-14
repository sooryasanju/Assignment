print("enter the list of fans separated by a space ")
x = [i for i in input().split()]
# print(x)
dict={}
y=[]
count=1
z=[]
for i in x:
    print("enter the dependancy of ",i," separated by a space (if there is no dependancy enter 0) ")
    y=[j for j in input().split()]
    if '0' in y:
        z.append(i)
    dict.update({i:y})
# print(dict)
for i in z:
    if i in dict:
        del dict[i]

# print(z)
# print(dict)
d={}
for x,y in dict.items():
    n=len(y)
    d.update({x:n})
# print(d)
for key,value in sorted(d.items(),key=lambda kv:kv[1]):
    z.append(key)
print("The order in which fan installation can be completed without conflicts is ",z)









