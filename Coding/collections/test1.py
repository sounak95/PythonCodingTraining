from itertools import combinations
S,K = map(str,raw_input().split())

for i in range(1,int(K)+1):
    for item in  list(combinations(list(sorted(S)),int(i))):
        print "".join(item)



