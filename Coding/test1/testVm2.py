l1=[3,7,7]
"""
o/p: 390
"""

# str1=""
# for item in l1:
#     str1+=str(item)
#
# print(int(str1)+1)

sum=0
carry=1
for i in range(len(l1)-1,-1,-1):
    # print(l1[i])
    temp=l1[i]+carry
    if temp==10:
        carry=1
        l1[i]=0
    else:
        carry=0
        l1[i]=temp

print(l1)

