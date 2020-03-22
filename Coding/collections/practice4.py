#https://www.hackerrank.com/challenges/word-order/problem
n= int(raw_input())
from collections import OrderedDict
my_order = OrderedDict()
for i in range(n):
    name=raw_input()
    if name not in my_order:
        my_order[name] = 1
    else:
        my_order[name] += 1
print len(my_order)
print ' '.join(map(str,my_order.values()))