arr = [5, 9, 4, 3, 6, 8, 10, 7, 9]

n=len(arr)
leftMax = [None]*n
leftMax[0] = float('-inf')
for i in range(1,n):
    leftMax[i]=max(leftMax[i-1],arr[i-1])
    print("leftMax of arr[{}], element {} is {}".format(i,arr[i],leftMax[i]))

rightMin=[None]*n
rightMin[n-1]=float('inf')

for i in range(n-2,-1,-1):
    rightMin[i] = min(rightMin[i+1],arr[i+1])
    print("leftMax of arr[{}], element {} is {}".format(i, arr[i], leftMax[i]))

