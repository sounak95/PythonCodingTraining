class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        sum=0
        for i in range(1,len(A)):
            x=abs(A[i]-A[i-1])
            y=abs(B[i]-B[i-1])
            sum+=max(x,y)
        return sum

s=Solution()
# A=map(int,raw_input().split()[1:])
# B=map(int,raw_input().split()[1:])
A = [ -7, -13 ]
B = [1 , -5]
s.coverPoints(A,B)

