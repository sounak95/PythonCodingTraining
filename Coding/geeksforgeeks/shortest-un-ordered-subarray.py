l1=[1,2,5,4,3]
print(l1)
print(sorted(l1))

pos1=-1
pos2=-1
index=-1
for x,y in zip(l1,sorted(l1)):
    index+=1
    if x != y:
        if pos1==-1:
            pos1=index
        else:
            pos2=index


# print(l1[pos1])
# print(l1[pos2])

for item in l1[pos1:pos2+1]:
    print(item)