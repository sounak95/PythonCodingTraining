#https://www.hackerrank.com/challenges/decorators-2-name-directory/problem

n=int(raw_input())

l=[]
for _ in range(n):
    l.append(raw_input().split())
# print l

from operator import itemgetter
K=sorted(l,key=itemgetter(-2))
# print K
for item in K:
    if (item[-1] == "M"):
        print "Mr. {} {}".format(item[0],item[1])
    elif (item[-1] == "F"):
        print "Ms. {} {}".format(item[0], item[1])
