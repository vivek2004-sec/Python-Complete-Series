import numpy as np

# array = np.array([1, 2, 3])

"""
Scalar arithmetic: scalar means single value.

"""


# print(array + 1)
# print(array - 2)
# print(array * 3)
# print(array ** 2)
# print(array / 2)
# print(array // 2)

"""
Vectorized maths functions:
"""

# array = np.array([1.23, 2.005, 3.987])
# print(np.sqrt(array))
# print(np.round(array))
# print(np.floor(array))
# print(np.ceil(array))
# print(np.pi)

# radii = np.array([1,2,3])
# print(np.pi * radii ** 2)

'''
Element-wise Arithmetic:
'''

array1 = np.array([1, 2, 3])
array2 = np.array([3, 5, 6])

print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1[0] + array2[2])