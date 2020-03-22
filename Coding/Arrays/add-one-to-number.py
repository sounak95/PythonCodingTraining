class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        if A[0] == 0 and len(A):
            return 1
        temp=""
        for item in A:
            temp+=str(item)
        return int(temp)+1
s=Solution()
A=[0]
print s.plusOne(A)

#Error in compiler
