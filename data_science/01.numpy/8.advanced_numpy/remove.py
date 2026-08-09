
import numpy as np

array = np.array([10, 20, 30, 40, 50])

new_arr = np.delete(array, 2, axis=None)
print(new_arr)


array2 = np.array([[1,2], [3,4]])
print(array2)
new_arr2 = np.delete(array2, 0, axis=0)
print(new_arr2)