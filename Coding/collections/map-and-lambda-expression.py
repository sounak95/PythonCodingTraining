count =2
n=5
a,b=0,1
l=[]
l.extend([a,b])
while(count<n):
    a,b=b,a+b
    # print a
    # print b
    # print "count: ", count
    l.append(b)
    count+=1

print list(map(lambda x:x**3, l))