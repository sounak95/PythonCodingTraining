#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/pairs-having-similar-element-eed098aa/description/

n=input()
l1= map(int, raw_input().split())

d={}

l3=[]
for i in range(len(l1)):
    for j in range(i+1,len(l1)):
        l = []
        if l1[i]==l1[j]+1 or l1[j]==l1[i]+1:
            # print "i:{} j:{}".format(i+1,j+1)
            d[i+1]=j+1
            l=[i+1,j+1]
            l3.append(l)

# print l3

l4=list(l3)
for i in range(len(l3)):
    a_set=set(l3[i])
    for j in range(i + 1, len(l3)):
        b_set=set(l3[j])
        if (len(a_set.intersection(b_set))) > 0:
            # print sorted(list(a_set.symmetric_difference(b_set)))
            l4.append(sorted(list(a_set.symmetric_difference(b_set))))
 
print len(l4)



# a=[1,2]
# b=[2,3]
# a_set = set(a)
# b_set = set(b)
#
# if (len(a_set.intersection(b_set)))>0:
#     print a_set.symmetric_difference(b_set)






