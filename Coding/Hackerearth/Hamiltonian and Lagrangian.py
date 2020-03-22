#https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/hamiltonian-and-lagrangian/
n=input()
l1=map(int, raw_input().split())
for i in range(len(l1)):
    flag=0
    for j in range(i+1,len(l1)):
        if l1[i]<=l1[j]:
            flag=1
            break
    if flag==0:
        print l1[i],

