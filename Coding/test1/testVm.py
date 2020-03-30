# l1=[5,6,1,9,2,13,14]

l1=[1,1,1,1]
first=second=third=-9999999

"""
TC1:

1. number of items in list is more than 3 handled
1.1 Repeating numbers with no third highest
1.2 Repeating numbers with no second highes
2. number of items in list is less than 3
3. number of items in list is less than 2


"""

if len(l1)<3:
    print("there is no third highest element")
elif(len(l1)<2):
    print("there is no second highest element")

for item in l1:
    if item>first:
        third=second
        second=first
        first=item
    elif(item>second and item!=first):
        third = second
        second = item
    elif(item>third and item!=second):
        third = item



if third==-9999999:
    print("there is no third highest element")
    print("First: {} Second: {}".format(first,second))
elif second==-9999999:
    print("there is no second highest element")
    print("First: {}".format(first))
else:
    print("First: {}, Second:{}, Third:{}".format(first,second,third))