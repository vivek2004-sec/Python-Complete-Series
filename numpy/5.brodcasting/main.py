import numpy as np

array1 = np.array([[1, 2, 3, 4]])
array2 = np.array([[1], [2], [3], [4]])

# print(array1.shape)
# print(array2.shape)

array3 = array1 * array2
print(array3)
print(array3.ndim)
print(array3.shape)
print(array3.size)