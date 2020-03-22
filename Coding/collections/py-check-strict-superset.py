set_A=set(map(int,raw_input().split()))
list1=[]
for _ in range(int(raw_input())):
    set_B = set(map(int, raw_input().split()))
    list1.append(set_A>set_B)
print list1
print all(list1)


