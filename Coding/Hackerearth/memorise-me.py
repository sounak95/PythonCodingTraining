#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/memorise-me/

n1=int(input())

l1=map(int, raw_input().split())

n2=int(input())

for _ in range(n2+1):
    n=l1.count(int(input()))
    if n ==0:
        print "NOT PRESENT"
    else:
        print n
