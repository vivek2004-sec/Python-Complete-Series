'''
np.concatenate((array1, array2), axis=0)

axis= 0 : gives the vertical stacking
axis=1 : gives the horizontal stacking
'''

import numpy as np

arr1 = np.array([1,2])
arr2 = np.array([3,4])
arr3 = np.concatenate((arr1, arr2), axis=0)
arr4 = np.concatenate((arr1, arr2), axis=None)
print(arr3)
print(arr4)