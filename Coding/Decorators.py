# def div(a,b):
#     print (a/b)
#
# def smart_div(func):
#     def inner(a,b):
#         if b>a:
#             a,b=b,a
#         return func(a,b)
#     return inner
#
# div=smart_div(div)
#
# div(4,2)
#
# l=[1,2,3,4,5]
# print(l *2)
#
import numpy as np
# np_mat = np.array([[1, 2],
#                    [3, 4],
#                    [5, 6]])
# print(np_mat * 2)
# print(np_mat * np.array([10, 11]))
# print(np_mat + np_mat)

height = np.round(np.random.normal(1.75, 0.20, 5000), 2)
weight = np.round(np.random.normal(60.32, 15, 5000), 2)
# print(height)
# print(weight)

print(np.array(np.column_stack((height, weight))).shape)