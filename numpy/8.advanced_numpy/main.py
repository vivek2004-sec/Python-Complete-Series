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