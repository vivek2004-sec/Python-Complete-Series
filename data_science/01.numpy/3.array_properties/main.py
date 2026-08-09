import numpy as np

# int_num = np.array([1.2, 2.3, 4.5])

# num = int_num.astype(int)
# print(num)
# print(num.dtype)

#  Array operations

# array = np.array([[1, 2, 3, 4, 5],
#                   [6, 7, 8, 9, 10]])
# print(array + 1)
# print(array - 1)
# print(array * 1)
# print(array / 1)
# print(array ** 1)
# print(array // 1)
# print(array % 2)


# Aggregation in numpy

array = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
print(np.sum(array))
print(np.mean(array))
print(np.median(array))
print(np.average(array))
print(np.min(array))
print(np.max(array))
print(np.std(array))