#https://www.geeksforgeeks.org/trapping-rain-water/

def findWater(arr,n):
    leftMax=[0]*n
    rightMax=[0]*n
    water=0
    leftMax[0]=arr[0]
    for i in range(n):
        leftMax[i]=max(leftMax[i-1],arr[i])

    rightMax[n-1]=arr[n-1]
    for i in range(n-2,-1,-1):
        rightMax[i]=max(rightMax[i+1],arr[i])

    for i in range(0,n):
        water+=min(leftMax[i],rightMax[i])-arr[i]
        print(min(leftMax[i],rightMax[i])-arr[i])

    return water


arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
n = len(arr)
print("Maximum water that can be accumulated is",findWater(arr, n))

