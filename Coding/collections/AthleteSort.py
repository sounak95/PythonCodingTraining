n,m=map(int,raw_input().split())
l1=[]
for _ in range(n):
    l1.append(map(int,raw_input().split()))
X=int(raw_input())
for item in sorted(l1,key=lambda x:x[X]):
    print " ".join(map(str,item))