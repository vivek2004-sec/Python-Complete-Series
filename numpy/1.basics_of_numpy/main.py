import numpy as np

# my_list = [1, 2, 3, 4]

# my_list = my_list * 2  # output: [1, 2, 3, 4, 1, 2, 3, 4]
# print(my_list)

array = np.array([1, 2, 3, 4])
print(type(array)) # <class 'numpy.ndarray'>

array = array * 2
print(array) # output: [2 4 6 8]

print("Dimensions:",array.ndim)