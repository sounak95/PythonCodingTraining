# print(ord("9")-ord("0"))

# def myAtoi(string):
#     res = 0
#
#     # Iterate through all characters of input string and
#     # update result
#     for i in range(len(string)):
#         # print ("i: {}".format(i))
#         res = res * 10 + (ord(string[i]) - ord('0'))
#         print(res)
#
#     return res
#
# # Driver program
# string = "89789"
# print(myAtoi(string))

# print("C:\TIProject\TIStandalone\\tita\\tests\Regression\Module\*"

# l1=[7, 3, 2, 4, 9, 12, 56]
# n=len(l1)
# for i in range(n):
#     for j in range(i+1,n+1):
#         print("{}".format(l1[i:j]))

import os

str1="abc_12.txt"
print(str1.find("_"))
print(str1.find("."))
print(str1[str1.find("_")+1:str1.find(".")])

path = os.getcwd()

max=float('-inf')
for r, d, f in os.walk(os.getcwd()):
    for file in f:
        if str(file).startswith("New Text Document",) and str(file).endswith(".txt"):
            str1=str(os.path.join(r, file))
            index=int(str1[-5])
            if index>max:
                max = index

print(str(max))
#             files.append(os.path.join(r, file))
#
# for f in files:
#     print(f)
#
