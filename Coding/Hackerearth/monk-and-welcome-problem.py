#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/monk-and-welcome-problem/

n=input()
l1=map(int, raw_input().split())
l2=map(int, raw_input().split())
l3=[]

for x,y in zip(l1,l2):
    l3.append(x+y)

for item in l3:
    print item,

