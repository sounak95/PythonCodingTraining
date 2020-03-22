#https://www.geeksforgeeks.org/rearrange-array-even-index-elements-smaller-odd-index-elements-greater/

l1=[6,4,2,1,8,3]

for i in range(len(l1)-1):
    if i%2==0:
        if l1[i]>=l1[i+1]:
            l1[i],l1[i+1]=l1[i+1],l1[i]
    else:
        if l1[i] <= l1[i + 1]:
            l1[i], l1[i + 1] = l1[i + 1], l1[i]

print(l1)