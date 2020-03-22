#https://www.geeksforgeeks.org/move-zeroes-end-array/

l1=[1,2,0,4,3,0,5,0,9,0,0,0]
count=0
for i, item in enumerate(l1):
    if item!=0:
        l1[count]=item
        count+=1

for i in range(count,len(l1)):
    l1[i]=0

print(l1)
