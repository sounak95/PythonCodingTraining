class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        A = [char for char in A]
        max=A.count("1")
        for i in range(len(A)-1):
            for j in range(i,len(A)):
                B = list(A)
                # print "{} {}".format(i+1,j+1)
                for k in range(i,j+1):
                    if A[k]=="0":
                        B[k]="1"
                    else:
                        B[k] = "0"
                # print B
                count =B.count("1")
                if count>max:
                    max=count
                    return i+1,j+1
                    # print "index: {} {}".format(i+1,j+1)
        return ""





s=Solution()
A="111"
# A=[int(char) for char in A]
# print A
print s.flip(A)