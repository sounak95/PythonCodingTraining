#https://www.geeksforgeeks.org/find-the-element-before-which-all-the-elements-are-smaller-than-it-and-after-which-all-are-greater-than-it/

def findElement(arr,n):
    leftMax=[None]*n
    leftMax[0]=float('-inf')

    for i in range(1,n):
        leftMax[i]=max(leftMax[i-1],arr[i-1])

    rightMin=float('inf')
    for i in range(n-1,-1,-1):
        if leftMax[i-1]<arr[i]<rightMin:
            return i

        rightMin=min(rightMin,arr[i])

# Driver program
if __name__ == "__main__":

    arr = [5, 1, 4, 3, 6, 8, 10, 7, 9]
    n = len(arr)
    print("Index of the element is", findElement(arr, n))