#https://www.geeksforgeeks.org/count-triplets-such-that-one-of-the-numbers-can-be-written-as-sum-of-the-other-two/

l1=[1,1,1,2,2]
count=0
for i in range(0,len(l1)-2):
    for j in range(i+1,len(l1)-1):
        for k in range(j+1,len(l1)):
            if (l1[k]==l1[i]+l1[j]) or (l1[j]==l1[i]+l1[k]) or (l1[i]==l1[j]+l1[k]):
                print("{} {} {}".format(l1[i],l1[j],l1[k]))
                count += 1
print(count)

