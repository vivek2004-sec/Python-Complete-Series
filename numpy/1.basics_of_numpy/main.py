import numpy as np

# my_list = [1, 2, 3, 4]

# my_list = my_list * 2  # output: [1, 2, 3, 4, 1, 2, 3, 4]
# print(my_list)

array = np.array([1, 2, 3, 4])
print(type(array)) # <class 'numpy.ndarray'>

array = array * 2
print(array) # output: [2 4 6 8]

print("Dimensions:",array.ndim)

# creating an array

num1 = np.zeros(3)
print(num1)

num2 = np.ones(3)
print(num2)

num3 = np.ones((2,3))
print(num3)

a = np.full((2, 2), 9)
print(a)

# creating sequences in numpy

arr = np.arange(1, 10, 2)
print(arr)

# creating identity matrices

identity = np.eye(3)
print(identity)