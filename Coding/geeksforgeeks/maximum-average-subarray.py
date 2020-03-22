#https://practice.geeksforgeeks.org/problems/maximum-average-subarray/0

# l1=[3,-435,335,10,-50,100,20]
# k=3
# max=-1
# pos1=-1
# pos2=-1
# for i in range(len(l1)-k+1):
#
#     avg= sum(l1[i:i+k])/k
#     if avg>max:
#         max=avg
#         pos1=i
#         pos2=i+k
#
# print l1[pos1:pos2]

n=int(input())

for _ in range(n):
    k=int(input())
    num_ele=int(input())
    l1=list(map(int, input().split()))
    # print(l1)
    max = -1
    pos1 = -1
    pos2 = -1
    for i in range(len(l1) - k + 1):

        avg = sum(l1[i:i + k]) / k
        if avg > max:
            max = avg
            pos1 = i
            pos2 = i + k

    str1=""
    count=0
    for item in l1[pos1:pos2]:
        count+=1
        if count==1:
            str1=str(item)
        else:
            str1+= " " + str(item)
    print (str1)
