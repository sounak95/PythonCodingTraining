num=-123

l=[]
if (num>0):
    for i in str(num):
        l.append(i)
elif(num<0):
    for i in str(num)[1:]:
        l.append(i)
# print(l)
s=0
e=len(l)-1


while (s < e):
    l[s], l[e] = l[e], l[s]
    s += 1
    e -= 1
if num>0:
    print("".join(l))
elif(num<0):
    ans="-"+"".join(l)
    print(ans)
else:
    print("0")

