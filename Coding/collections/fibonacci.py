a=0
b=1
count=1
l1=[]
n=int(raw_input())
l1.extend([a,b])
while(count<n):
    a,b=b,a+b
    # print b
    l1.append(b)
    count+=1

print map(lambda x:x**3, l1)