"""
np.insert(array, index, value, axis= none)
for 1D array :
axis = none

for 2D array:
axis = 0 -> row wise
axis = 1 -> column wise
"""
import numpy as np

array = np.array([10, 20, 30, 40, 50, 60])
new_array = np.insert(array, 2, 35, axis=None)
print(new_array)

array2 = np.array([[1, 2, 3],
                   [4, 5, 6]])
print(array2)
new_arr = np.insert(array2, 1, [5, 6, 7], axis=0)
print(new_arr)

arr_2 = np.array([[1, 2],
                  [3, 5]])
print(arr_2)
new_arr_2 = np.insert(arr_2, 2, [4, 6], axis=1)
print(new_arr_2)