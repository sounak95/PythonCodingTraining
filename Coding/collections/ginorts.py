#https://www.hackerrank.com/challenges/ginorts/problem

str1=raw_input()
lower=[]
upper=[]
odd=[]
even=[]
for ch in str1:
    if ch.isdigit():
        if int(ch)%2==0:
            even.append(int(ch))
        else:
            odd.append(int(ch))
    elif ch.isalpha():
        if ch.islower():
            lower.append(ch)
        else:
            upper.append(ch)
lower.sort()
upper.sort()
odd.sort()
even.sort()
print "".join(map(str,lower+upper+odd+even))
