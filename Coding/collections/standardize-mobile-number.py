n=int(raw_input())
l1=[]
for _ in range(n):
    str1=raw_input()
    l1.append("+91 " + str1[-10:-6] + str1 [-6:])
l1.sort()
print "\n".join(l1)
