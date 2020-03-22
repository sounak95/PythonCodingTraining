from collections import OrderedDict
n=int(raw_input())
d=OrderedDict()
for _ in range(n):
    str1=raw_input()
    if str1 in d:
        d[str1]+=1
    else:
        d[str1]=1

print len(list(d.keys()))
print " ".join(list(map(str,d.values())))