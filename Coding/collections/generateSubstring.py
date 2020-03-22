str1="BANANA"
n=len(str1)
l1=[]
for i in range(n):
    for j in range(i,n):
        l1.append(str1[i:j+1])
        print str1[i:j+1]
s=set(l1)
print len(l1)
print l1