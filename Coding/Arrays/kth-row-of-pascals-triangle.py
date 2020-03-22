A=5
len=A
a=[]
for i in range(2,0,-1):
    l= [0 for _ in range(len-i+1)]
    a.append(l)

len1=[1]
a[0]=[1]

for i in range(1,len):
    k=1
    count=0
    for j in range(i+1):
        count+=1
        if (i-1)>=0 and (j-1)>=0:
            if j<len1[i-1]:
                # print i
                # print j
                res=(a[k-1][j-1]+a[k-1][j])
                a[k][j]=res
            else:
                # print j
                a[k][j] = 1
        else:
            a[k][j] =1
    len1.append(count)
    print a
    a[k-1]=a[k]



for item in a :
    print item