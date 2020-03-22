class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, nums):
        flag = 0
        sorted_nums = sorted(nums)
        left, right = float('inf'), float('-inf')
        for i in xrange(len(nums)):
            if nums[i] != sorted_nums[i]:
                if flag==0:
                    left = min(left, i)
                flag=1
                right = max(right, i)

        return [left, right] if left != float('inf') else [-1]

s=Solution()
nums=[1,2,3]
print s.subUnsort(nums)