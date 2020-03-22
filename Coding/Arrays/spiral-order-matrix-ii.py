
len=4
a=[[0 for i in range(len)] for i in range (len)]
# print a
top_left_i=0
top_left_j=0
top_right_i=0
top_right_j=len-1
bottom_left_i=len-1
bottom_left_j=0
bottom_right_i=len-1
bottom_right_j=len-1

count=1

while count<=len**2:
    for i in range(top_left_j,top_right_j+1):
        a[top_left_i][i]=count
        count+=1

    # for item in a:
    #     print item
    #
    # print "Debug"

    for i in range(top_right_i+1, bottom_right_i + 1):
        a[i][top_right_j] = count
        count += 1

    # for item in a:
    #     print item
    #
    # print "Debug"

    for i in range(bottom_right_j-1, bottom_left_j-1 ,-1):
        a[bottom_right_i][i] = count
        count += 1

    # for item in a:
    #     print item
    #
    # print "Debug"

    for i in range(bottom_left_i-1, top_left_i,-1):
        a[i][bottom_left_j] = count
        count += 1

    # for item in a:
    #     print item
    #
    # print "Debug"

    top_left_i+=1
    top_left_j +=1
    top_right_i +=1
    top_right_j -=1
    bottom_left_i -=1
    bottom_left_j +=1
    bottom_right_i -=1
    bottom_right_j -=1

    # print a

for item in a:
    print item
