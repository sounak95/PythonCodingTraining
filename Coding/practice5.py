m = int(raw_input())
set_m = set(map(int,raw_input().split()))
n = int(raw_input())
set_n = set(map(int,raw_input().split()))
print len(set_m.difference(set_m.intersection(set_n)))
