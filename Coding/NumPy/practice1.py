import numpy as np

#https://github.com/KeithGalli/NumPy/blob/master/NumPy%20Tutorial.ipynb

# a = np.array([1,2,3], dtype='int32')
# print(a)
#
# b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
# print(b)
#
# print(a.ndim)
#
# print(b.shape)
#
# print(a.dtype)
#
# print(a.itemsize)
#
# print(a.nbytes)
#
# print(a.size)

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
# print(a)
#
# print(a[1, 5])
#
# print(a[0,:])
#
# print(a[:, 2])
#
# print(a[0,1:-1:2])
#
# a[1,5]=20
#
# a[:,2] = [1,2]
#
# print(a)

# b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
#
# print(b)
#
# print(b[0,1,1])
#
# b[:,1,:] = [[9,9],[8,8]]
#
# print(b)

# print(np.zeros((2,3)))
# print(np.ones((4,2,2), dtype='int32'))
#
# print(np.full((2,2), 99))
#
# print(np.full_like(a, 4))
#
# print(np.random.randint(-4,8, size=(3,3)))
#
# print(np.identity(5))
#
# arr = np.array([[1,2,3]])
# r1 = np.repeat(arr,3, axis=0)
# print(r1)

# output = np.ones((5,5))
# print(output)
#
# z = np.zeros((3,3))
# z[1,1] = 9
# print(z)
#
# output[1:-1,1:-1] = z
# print(output)

# a = np.array([1,2,3])
# b = a.copy()
# b[0] = 100
#
# print(a)

# a = np.array([1,2,3,4])
# print(a)
#
# print(a+2)
# print(a-2)
# print(a*2)
# print(a/2)

# b = np.array([1,0,1,0])
# print(a + b)
#
# print(a**2)
#
# print(np.cos(a))

# For a lot more (https://docs.scipy.org/doc/numpy/reference/routines.math.html)

# a = np.ones((2,3))
# print(a)
#
# b = np.full((3,2), 2)
# print(b)
#
# np.matmul(a,b)

# stats = np.array([[1,2,3],[4,5,6]])
#
# print(np.min(stats))
# print(stats)
# print(np.max(stats, axis=1))
#
# print(np.sum(stats, axis=0))

before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)

after = before.reshape((4,2))
print(after)

v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

print(np.vstack([v1,v2,v1,v2]))

#Horizontal  stack
h1 = np.ones((2,4))
h2 = np.zeros((2,2))

print(h1)
print(h2)
print(np.hstack((h1,h2)))
# print(np.vstack((h1,h2)))

