m,n = map(int,raw_input().split())
l=[]
for _ in range(m):
    l.append(map(int,raw_input().split()))
k= int(raw_input())
l = sorted(l,key=lambda x:x[k] )
print l
for item in l:
    print " ".join(str(k) for k in item)