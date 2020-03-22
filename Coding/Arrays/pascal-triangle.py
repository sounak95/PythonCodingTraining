A=5
len=A
a=[]
for i in range(len):
    l= [0 for _ in range(i+1)]
    a.append(l)
# for i in range(len):
#     print len(a[i:i+1])
len1=[]
for i in range(len):
    count=0
    for j in range(i+1):
        count+=1
        if (i-1)>=0 and (j-1)>=0:
            if j<len1[i-1]:
                # print i
                # print j
                a[i][j]=a[i-1][j-1]+a[i-1][j]
            else:
                a[i][j] = 1
        else:
            a[i][j] =1
    len1.append(count)

for item in a :
    print item