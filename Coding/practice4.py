n= int(raw_input())
set1 = set(map(int, raw_input().split()))
m= int(raw_input())
print m
for i in range(m):
    a= raw_input()
    if "pop" in a:
        # print "popping"
        set1.pop()
    elif("remove" in a):
        # print "removing {}".format()
        set1.remove(int(a.split()[1]))
    elif ("discard" in a):
        set1.discard(int(a.split()[1]))
print set1
print sum(set1)
