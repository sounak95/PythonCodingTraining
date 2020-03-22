n=int(raw_input())
list1=map(int, raw_input().split())
max1=max(list1)
sec_max=-99999999
for item in list1:
    if item!=max1 and item>sec_max:
        sec_max=item
print sec_max
