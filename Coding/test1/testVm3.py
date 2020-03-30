"""
[[1,2,3,4], [5,6,7,8], [9,10,11,12]]

[[1,5,9],[2,6,10],[],[]]

-- list comprehension




"""

l1=[[1,2,3,4], [5,6,7,8], [9,10,11,12]]
l2=[]
rows=len(l1)
# print(rows)
cols=len(l1[0])
# print(cols)

for j in range(cols):
    temp_list=[]
    for i in range(rows):
        # print(l1[i][j])
        temp_list.append(l1[i][j])
    l2.append(temp_list)

print(l2)

l4=[[]]
l3=[[l1[j][i] for j in range(rows)] for i in range(cols)]

print(l3)

# for i in range(rows):
#     temp_list=[]
#     for j in range(cols):
#         l1[i][j]=l1[j][i]
# print(l1)

