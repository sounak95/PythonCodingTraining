#https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
from collections import defaultdict
d = defaultdict(list)
# d={}
list1=[]


n, m = map(int,raw_input().split())

for i in range(0,n):
    d[raw_input()].append(i+1)

for i in range(0,m):
    list1.append(raw_input())

for i in list1:
    if i in d:
        print " ".join( map(str,d[i]) )
    else:
        print -1