#https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
from collections import OrderedDict
my_order = OrderedDict()
for i in range(int(raw_input())):
    line = raw_input().split()
    name = int(line[-1])
    price = ' '.join(line[0:-1])
    if name not in my_order:
        my_order[name] = int(price)
    else:
        my_order[name] += int(price)
for item_name, net_price in my_order.items():
    print item_name,net_price