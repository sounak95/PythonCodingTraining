A=[[1,2,3],[4,5,6],[7,8,9]]
n=len(A)
list1=[[] for _ in range(2*n-1)]
for i in range(0,n):
    for j in range(0,n):
        list1[i+j].append(A[i][j])

for item in list1:
    print item
