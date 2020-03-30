# str1="1387321792"
#
# n=len(str1)
# visited=[False]*n
# for i in range(n):
#     ch=str1[i]
#     count=1
#     if visited[i]==True:
#         continue
#     for j in range(i+1,n):
#         if(str1[i]==str1[j]):
#             count+=1
#             visited[j]=True
#
#     print("frequency of {} is {}".format(ch,count))


str1="13 85 71 348"

"""
31 85 71 843
"""

l1=str1.split(" ")

def mysort(l1):
    a=list(l1)
    n=len(a)
    str11=""
    for i in range(n-1):
        for j in range(n-1-i):
            if a[j]<a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    # return("".join(a))
    for item in a:
        str11+=item
    return  str11

# print(mysort("1263"))

strTemp=""
for item in l1:
    strTemp = strTemp + mysort(item) + " "

print(strTemp)


