#https://www.hackerrank.com/challenges/symmetric-difference/problem
m= map(int,raw_input())
set_m= set(map(int, raw_input().split()))
n= map(int,raw_input())
set_n= set(map(int, raw_input().split()))
# set_comm = set_m.intersection(set_n)
set_test1 = set_m.difference(set_n)
set_test2 = set_n.difference(set_m)
print sorted(set_test1.union(set_test2))


