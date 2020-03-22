# A = [1,2,3]
# B = [6,5,4]
# C = [7,8,9]
# X = [A] + [B] + [C]
# print zip(*X)
#
# for a,b,c in zip(A,B,C):
#     print a,b,c

# a=121
# print str(a)==reversed(str(a))
# print str(a)
# print all(s==t for s,t in zip(str(a),reversed(str(a))))
# for item in reversed(str(a)):
#     print item


# a=17
# print "{0:x}".format(a)

# str1="SOUNAK"
#
# for i in range(len(str1)-1,-1,-1):
#     print str1[i]

# line = map(int,raw_input().split(" "))
str1 = "ABCDCDC"
str2= "CDC"
def count_substring(string, sub_string):
    count=0
    n=len(string)
    m=len(sub_string)
    for i in range(n-m):
        for j in range(m):
            if(string[i+j]!=sub_string[j]):
                break
        if(j==m-1):
            count+=1
    return count
print(count_substring(str1,str2))
