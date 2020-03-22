#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/charged-up-array-f35a5e23/

# Python program to print all
# sublist from a given list

# function to generate all the sub lists
def sub_lists(list1):

    # store all the sublists
    sublist = []

    # first loop
    for i in range(len(list1) ):

        # second loop
        for j in range(i + 1, len(list1)+1):

            # slice the subarray
            sub = list1[i:j]
            sublist.append(sub)


    return sublist

# driver code
# l1 = [1,2,3]
# print(sub_lists(l1))

import math;



def powerset(s):
    l1=[]
    x = len(s)
    for i in range(1 << x):
        l1.append([s[j] for j in range(x) if (i & (1 << j))])
    return l1


n=int(input())
for _ in range(n):
    num_elements=int(input())
    l= map(int, raw_input().split())
    l1 = powerset(l)
    sum = 0
    for num in l:
        count = 0
        for item in l1:
            if num in item:
                count += 1
                # print "{} present in {}".format(num,item)
        # print "{} is present in {} subsets".format(num,count)
        if num >= count:
            sum += num
    print sum
# l=[3,4,5]
# l1 = powerset(l)
# sum=0
# for num in l:
#     count=0
#     for item in l1:
#         if num in item:
#             count+=1
#             # print "{} present in {}".format(num,item)
#     # print "{} is present in {} subsets".format(num,count)
#     if num>=count:
#         sum+=num
# print sum
#
