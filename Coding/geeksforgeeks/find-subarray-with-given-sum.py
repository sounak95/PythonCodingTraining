
#https://www.geeksforgeeks.org/find-subarray-with-given-sum/

l1=[1,4,20,3,10,5]

curr_sum=0
sum=33
flag=0
for i,item in enumerate(l1):
    curr_sum = item
    for j in range(i+1,len(l1)):
        if curr_sum==sum:
            print( "sum {} found between index {} and {}".format(sum,i,j-1))
            flag=1
            break
        if (curr_sum>sum) or (j==len(l1)):
            break
        curr_sum += l1[j]

if flag==0:
    print("No sub array found")


