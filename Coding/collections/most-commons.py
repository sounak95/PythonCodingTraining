str1=raw_input()
letters=[0]*26
# print letters

for char in str1:
    letters[ord(char)-ord('a')]+=1

# print letters

for i in range(3):
    # print "i: {}".format(i)
    a=max(letters)
    for i,item in enumerate(letters):
        if item==a:
            letters[i]=-1
            print "{} {}".format(chr(i+ord('a')), a)
            break
