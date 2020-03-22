


n=input()

str1=str(raw_input())
l1=list(str1)
ele="#"
flag=1
while(flag==1):
    for index in range(len(l1)-1):
        if l1[index]==l1[index+1]:
            l1[index]="#"
            l1[index+1]="#"

    while(ele in l1):
        l1.remove(ele)
    # print l1

    flag=0

    for index in range(len(l1) - 1):
        if l1[index] == l1[index + 1]:
            flag=1

str1=""

for item in l1:
    str1+=item
print len(l1)
print str1



