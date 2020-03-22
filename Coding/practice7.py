sup_set= set([1,2,3,4,5,6,7,8,9,10,11,12,23,45,84,78])
set1=set([1,2,3,4,5])
set2=set([78,11,12])
print((sup_set>set1) & (sup_set>set2))

import collections
x=[1,2,2,20,6,210]
print set(x)
a = collections.OrderedDict.fromkeys(x)
print collections.OrderedDict.fromkeys(x)