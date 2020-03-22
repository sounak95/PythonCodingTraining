#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/range-query-2/

def binaryToDecimal(binary):
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    # print(decimal)
    return decimal


def listToStr(l1):
    str1=""
    for item in l1:
        str1 += str(item)
    return int(str1)

n1,n2=map(int, raw_input().split())

l1=map(int, raw_input().split())

for _ in range(n2):
    x = map(int, raw_input().split())
    if x[0]==1:
        index=x[1]-1
        if l1[index]==0:
            l1[index] =1
        else:
            l1[index] = 0
    elif x[0]==0:
        l=x[1]-1
        r=x[2]-1
        result = l1[l:r+1]

number= binaryToDecimal(listToStr(result))
if number%2==0:
    print "EVEN"
else:
    print "ODD"

# print binaryToDecimal(listToStr(l1))

