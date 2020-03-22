from collections import Counter,defaultdict
n=int(raw_input())
l1=[]
l1=map(int,raw_input().split())
# print l1
dic1=defaultdict(list)
dic1= dict(Counter(l1))

m=int(raw_input())
sum=0
for i in range(m):
    temp=raw_input().split()
    size = int(temp[0])
    price = int(temp[1])
    if size in dic1:
        if dic1[size]>=1:
            sum+=price
            dic1[size]-=1

print sum