n=int(raw_input())
l=[]
s=set()
for _ in range(n):
    name= raw_input()
    marks = float(raw_input())
    s.add(marks)
    l.append([name,marks])
# print l
s=sorted(s)

# print s[1]
for item in sorted(l,key=lambda x:x[0]):
    if item[1]==s[1]:
        print item[0]


